from celery import shared_task
import subprocess
import os
import json
from .models import News, Tag
from django_celery_beat.models import PeriodicTask, IntervalSchedule


@shared_task
def fetch_and_store_news():
    spider_path = os.path.join(
        os.path.dirname(__file__), './../../zoomitscapar')

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
        tags = item.get('tags', [])
        source = item.get('url')

        # Create the News instance without tags
        news_instance = News.objects.create(
            title=title, body=description, source=source)

        # Create or get tags
        tags = [Tag.objects.get_or_create(name=tag)[0] for tag in tags]
        news_instance.tags.set(tags)

    if os.path.exists(os.path.join(spider_path, 'result.json')):
        os.remove(os.path.join(spider_path, 'result.json'))

    print(f"------- DONE. {len(news_items)
                           } items have been added to the database")
