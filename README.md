# AI-Powered PDF Analyzer

A Django REST Framework API that extracts content from PDF files and uses AI to generate concise summaries and questions. Built for teachers and students to quickly transform PDF documents into structured learning material. Generate AI-generated study material through a simple REST API.
 
## Features

- Extracts text from uploaded PDF files
- Generates AI-powered summaries
- Generate unique questions for learning and assessment
- Built with Django and Django REST Framework
- Async task support using Celery
- Containerized with Docker

## Tech Stack
- Django
- Django REST frameworks
- Celery
- Docker
  
## Docker Setup

The project is fully Dockerized for easy setup and deployment.

### Run with Docker Compose

```bash
docker compose up --build
```
API will be available at:
```
http://localhost:8000/
```
## Environment Variables

Create a .env file:
```
RABBITMQ_USER=Username
RABBITMQ_PASSWORD=Password
HF_ACCESS_TOKEN=

CELERY_BROKER_URL=amqp://Username:Password@rabbitmq:5672//
CELERY_RESULT_BACKEND=django-db
```
