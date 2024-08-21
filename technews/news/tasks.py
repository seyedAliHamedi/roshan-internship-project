from celery import shared_task
import subprocess
import os
import json
from .models import News, Tag
from django_celery_beat.models import PeriodicTask, IntervalSchedule


@shared_task
def fetch_and_store_news():
    spider_path = os.path.join(
        os.path.dirname(__file__), '../../zoomitscapar')

    command = ["scrapy", "crawl", "zoomit", "-o", "result.json"]

    subprocess.run(command, cwd=spider_path)

    news_items = []
    with open(os.path.join(spider_path, 'result.json'), 'r', encoding='utf-8') as f:
        content = f.read()
        try:
            news_items = json.loads(content)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")

    for item in news_items:
        title = item.get('title')
        description = item.get('description')
        categories = item.get('categories', [])
        source = item.get('url')

        # Create the News instance
        news_instance = News.objects.create(
            title=title, body=description, source=source)

        # Get or create tags and assign them to the news instance
        tags = [Tag.objects.get_or_create(name=tag)[0] for tag in categories]
        news_instance.tags.set(tags)

    print(f"DONE. {len(news_items)} items have been added to the database")
