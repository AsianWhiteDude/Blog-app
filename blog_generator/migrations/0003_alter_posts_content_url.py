# Generated by Django 5.0.4 on 2024-06-30 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_generator', '0002_remove_posts_content_posts_content_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='content_url',
            field=models.URLField(max_length=500),
        ),
    ]
