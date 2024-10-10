# Project overview
Developed a web application called "Blog Generator," which allows users to convert a YouTube video link into a structured article using artificial intelligence. During the creation of this application, I achieved the following goals:

- Implemented the project using Python and the Django framework.
- Organized interaction with the PostgreSQL database and stored "heavy" data in AWS Yandex Object Storage, saving links to them in the database as metadata.
- Utilized several APIs (AssemblyAI, YandexGPT, Yandex S3 Storage, Yandex Mail) to enhance the application's functionality.
- Set up Dockerfile and Docker Compose files for convenient deployment of the application.
- Ensured the stability and performance of the application using Nginx and Gunicorn.

# Cloning a repository

Cloning: Clone your private copy of the repository to your local machine:

```
git clone https://github.com/AsianWhiteDude/Blog-app.git
cd Blog-app
```

# Deploy
Docker Compose: Docker Compose is used to deploy the application.

```
docker compose up -d
```

This will start the container in the background with the specified services.

## Post-deploy update:

To apply changes on upgrade:

```
docker compose down
```
Delete all images and volumes

```
docker compose up -d
```
