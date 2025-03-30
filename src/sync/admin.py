from django.contrib import admin

from src.sync.models import SyncResult


@admin.register(SyncResult)
class SyncResultAdmin(admin.ModelAdmin):
    list_display = ("sync_date", "new_events_count", "updated_events_count")
    list_filter = (
        "sync_date",
        "new_events_count",
        "updated_events_count",
    )
    search_fields = (
        "sync_date",
        "new_events_count",
        "updated_events_count",
    )
