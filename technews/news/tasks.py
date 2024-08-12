from celery import shared_task
import subprocess
import os
import json
from .models import News
from django_celery_beat.models import PeriodicTask, IntervalSchedule


@shared_task
def fetch_and_store_news():
    print("HHHHHHHHHH")
    spider_path = os.path.join(
        os.path.dirname(__file__), '../../zoomitscapar')

    command = ["scrapy", "crawl", "zoomit", "-o", "result.json"]

    subprocess.run(command, cwd=spider_path)

    news_items = None
    with open(os.path.join(spider_path, 'result.json'), 'r', encoding='utf-8') as f:
        news_items = json.load(f)

    for item in news_items:
        title = item.get('title')
        description = item.get('description')
        tags = ', '.join(item.get('categories', []))
        source = item.get('url')

        News.objects.create(title=title, body=description,
                            tags=tags, source=source)

    print(f"DONE. {len(news_items)} items have been added to the database")
