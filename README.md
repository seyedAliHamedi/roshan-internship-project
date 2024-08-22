# Tech News Backend Project

This project is a backend implementation for a hypothetical news website, "Tech News." The project involves creating a REST API, collecting news data from the Zoomit website, and integrating Celery for periodic tasks. The backend is developed using Django and Django REST Framework, and the project is Dockerized for easy deployment.

## Project Overview

The project is divided into three main challenges:

### Challenge 1: Implementing a REST API

In this challenge, the goal is to implement a REST API using Django and Django REST Framework. The API should return a list of news articles, where each article includes the title, content, and associated tags. The tasks include:

- Designing and implementing the database model.
- Creating the API to list news articles.
- Adding filtering options based on tags.
- Writing unit tests for the project.

#### API Endpoints:

- **GET** `/api/news/` - Retrieve a list of all news articles.
- **GET** `/api/news/<id>/` - Retrieve a specific news article by ID.
- **POST** `/api/news/` - Create a new news article.
- **PUT** `/api/news/<id>/` - Update an existing news article by ID.
- **DELETE** `/api/news/<id>/` - Delete a news article by ID.
- **GET** `/api/tags/` - Retrieve a list of all tags.
- **GET** `/api/news/?tag=<tag_name>` - Filter news articles by a specific tag.

### Challenge 2: Collecting News Data

The second challenge focuses on data collection from the Zoomit news website through web scraping. The aim is to gather news articles using the Scrapy library and create a function that returns the list of news articles while considering the features from the previous challenge.

### Challenge 3: Adding Celery and Dockerization

The third challenge involves integrating Celery with Django to continuously update the news data in the database by scraping new articles. This challenge includes:

- Learning to use a message broker like Redis or RabbitMQ.
- Monitoring tasks with Celery Flower.
- Dockerizing the project using Dockerfile and Docker Compose.
