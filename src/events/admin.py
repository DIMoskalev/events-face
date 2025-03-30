from django.contrib import admin

from src.events.models import Playground, PlaygroundEvent


@admin.register(Playground)
class PlaygroundAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_filter = ("title",)
    search_fields = ("title",)


@admin.register(PlaygroundEvent)
class PlaygroundEventAdmin(admin.ModelAdmin):
    list_display = ("title", "date", "status", "playground")
    list_filter = (
        "title",
        "status",
        "date",
        "playground",
    )
    search_fields = (
        "title",
        "date",
        "playground",
    )
