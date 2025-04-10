# Generated by Django 5.1.7 on 2025-03-27 21:50

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Playground",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
            ],
            options={
                "verbose_name": "Площадка",
                "verbose_name_plural": "Площадки",
            },
        ),
        migrations.CreateModel(
            name="PlaygroundEvent",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Идентификатор",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="Название")),
                ("date", models.DateTimeField(verbose_name="Дата")),
                (
                    "status",
                    models.CharField(
                        choices=[("Открыто", "Открыто"), ("Закрыто", "Закрыто")],
                        default="Открыто",
                        max_length=255,
                        verbose_name="Статус",
                    ),
                ),
                (
                    "playground",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="events.playground",
                        verbose_name="Площадка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Событие",
                "verbose_name_plural": "События",
            },
        ),
    ]
