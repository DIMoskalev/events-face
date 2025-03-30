from django.urls import path

from .views import PlaygroundEventListView

urlpatterns = [
    path("api/events/", PlaygroundEventListView.as_view(), name="event-list"),
]
