from django.db import models
from django.utils import timezone


class SyncResult(models.Model):
    sync_date = models.DateTimeField(default=timezone.now)
    new_events_count = models.IntegerField(default=0)
    updated_events_count = models.IntegerField(default=0)

    def __str__(self):
        return (f"Синхронизировано {self.sync_date}"
                f"Новых: {self.new_events_count},"
                f"Обновленных: {self.updated_events_count}")

    class Meta:
        verbose_name = "Результат синхронизации"
        verbose_name_plural = "Результаты синхронизации"
