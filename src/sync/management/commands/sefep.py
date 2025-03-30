from datetime import datetime, timedelta

import requests
from django.core.management.base import BaseCommand
from django.utils import timezone

from src.events.models import PlaygroundEvent
from src.sync.models import SyncResult


class Command(BaseCommand):
    help = "Синхронизация событий с сервера"

    def add_arguments(self, parser):
        parser.add_argument("--date", type=str)
        parser.add_argument("--all", action="store_true")

    def handle(self, *args, **options):
        sync_date = options["date"]
        if sync_date:
            sync_date = datetime.strptime(sync_date, "%Y-%m-%d").date()
        else:
            sync_date = (timezone.now() - timedelta(days=1)).date()  # Вчерашняя дата

        url = "https://events.k3scluster.tech/api/events/"
        if not options["all"]:
            url += f"?changed_at={sync_date}"

        self.fetch_url(url)
        self.stdout.write(self.style.SUCCESS("События синхронизированы"))

    def fetch_url(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR("Ошибка получения событий с сервера"))
            return
        next_page = response.json().get("next")
        results = response.json().get("results")
        self.load_events(results)
        if next_page:
            self.fetch_url(next_page)

    def load_events(self, results):
        new_events_count = 0
        updated_events_count = 0

        for event_data in results:
            # Обработка мероприятия
            event, created = PlaygroundEvent.objects.update_or_create(
                id=event_data["id"],
                title=event_data["name"],
                date=datetime.fromisoformat(event_data["changed_at"]),
                status=event_data["status"],
            )
            if created:
                new_events_count += 1
            else:
                updated_events_count += 1

        # Логирование результатов синхронизации
        SyncResult.objects.create(
            sync_date=timezone.now(),
            new_events_count=new_events_count,
            updated_events_count=updated_events_count,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f"Синхронизация завершена: {new_events_count} новых событий, {updated_events_count} обновленных событий."
            )
        )
