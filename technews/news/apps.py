from django.apps import AppConfig


class NewsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'news'

    def ready(self):
        self.create_periodic_task()

    def create_periodic_task(self):
        from django_celery_beat.models import PeriodicTask, IntervalSchedule
        from django.db.utils import OperationalError
        try:
            schedule, created = IntervalSchedule.objects.get_or_create(
                every=1,
                period=IntervalSchedule.MINUTES,
            )
            PeriodicTask.objects.get_or_create(
                interval=schedule,
                name='Fetch and store news every minute',
                task='news.tasks.fetch_and_store_news',
            )
        except OperationalError:
            pass
