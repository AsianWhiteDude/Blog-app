import json
import os.path
import uuid
import requests
import assemblyai as aai

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseForbidden
from django.shortcuts import render
from pytube import YouTube
from dotenv import load_dotenv
from .models import Posts

load_dotenv()

aai.settings.api_key = os.getenv('ASSEMBLYAI_API_KEY')
cat_api_id = os.getenv('YAGPT_CAT_API_KEY')
yagpt_api_key = os.getenv('YAGPT_API_KEY')


@login_required
def index(request):
    return render(request, 'blog_generator/index.html', context={'title': 'Blog Generator'})


# add caching
def generate_blog(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            yt_link = data['link']
        except (KeyError, json.JSONDecodeError):
            return JsonResponse({'error': 'Invalid data sent'}, status=400)

        # get youtube title
        title = get_yt_title(yt_link)

        # get transcript
        transcription = get_transcription(yt_link)
        if not transcription:
            return JsonResponse({'error': 'Failed to get transcript'}, status=500)

        # use AI to generate the blog
        blog_content = generate_blog_from_transcription(transcription)
        if not blog_content:
            return JsonResponse({'error': 'Failed to generate blog article'}, status=500)
        # save blog article to the database
        new_blog_post = Posts.objects.create(
            user=request.user,
            yt_title=title,
            yt_link=yt_link,
            content=blog_content,
        )
        new_blog_post.save()
        # return blog article as a response

        return JsonResponse({'content': blog_content})

    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_yt_title(link):
    yt = YouTube(link)
    title = yt.title
    return title


def download_audio(link):


    yt = YouTube(link)
    video = yt.streams.filter(only_audio=True).first()

    unique_id = generate_random_string()
    file_name = f"audio_{unique_id}.mp3"

    out_file = video.download(output_path=settings.MEDIA_ROOT, filename=file_name)
    return out_file




def get_transcription(link):
    audio_file = download_audio(link)
    config = aai.TranscriptionConfig(language_code='ru')
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(audio_file)

    # delete file after getting the transcript
    if os.path.exists(audio_file):
        os.remove(audio_file)

    return transcript.text


def generate_blog_from_transcription(transcription):


    prompt = {
        "modelUri": f"gpt://{cat_api_id}/yandexgpt-lite",
        "completionOptions": {
            "stream": False,
            "temperature": 0.6,
            "maxTokens": "2000"
        },
        "messages": [
            {
                "role": "system",
                "text": "Основываясь на приведенной ниже расшифровке видео с YouTube,"
                        " напишите краткую статью в блоге, напишите ее на основе расшифровки, "
                        "сделайте так, чтобы это выглядело как настоящая статья в блоге."
            },
            {
                "role": "user",
                "text":  transcription
            }
        ]
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {yagpt_api_key}"
    }

    response = requests.post(url, headers=headers, json=prompt)
    response_from_gpt = response.text
    dict_from_gpt = json.loads(response_from_gpt)
    result = dict_from_gpt['result']['alternatives'][0]['message']['text']
    return result

def generate_random_string():
    random_string = str(uuid.uuid4())
    return random_string

def all_blogs(request):
    blog_articles = Posts.objects.filter(user=request.user)
    return render(request, 'blog_generator/all_blogs.html',
                  context={'title': 'AI Blog Generator',
                           'blog_articles': blog_articles})


def post_details(request, pk):
    blog_article = Posts.objects.get(id=pk)
    if request.user == blog_article.user:
        return render(request, 'blog_generator/blog_details.html',
                  context={'title': 'AI Blog Generator',
                           'blog_article': blog_article})
    else:
        return HttpResponseForbidden('<h1>403 Forbidden</h1>')