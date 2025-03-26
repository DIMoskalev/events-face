import uuid

from django.db import models

NULLABLE = {"blank": True, "null": True}


class Playground(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    title = models.CharField(max_length=255, verbose_name="Название")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Площадка'
        verbose_name_plural = 'Площадки'


class PlaygroundEvent(models.Model):

    OPEN = "Открыто"
    CLOSE = "Закрыто"

    STATUS_CHOICES = [
        (OPEN, "Открыто"),
        (CLOSE, "Закрыто"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, verbose_name="Идентификатор")
    title = models.CharField(max_length=255, verbose_name="Название")
    date = models.DateTimeField(verbose_name="Дата")
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default=OPEN, verbose_name="Статус")
    playground = models.ForeignKey(Playground, on_delete=models.CASCADE, **NULLABLE, verbose_name="Площадка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
