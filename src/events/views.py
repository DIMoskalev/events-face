from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions
from rest_framework.filters import OrderingFilter

from .models import PlaygroundEvent
from .paginators import PlaygroundEventsPaginator
from .serializers import PlaygroundEventSerializer


class PlaygroundEventListView(generics.ListAPIView):
    queryset = PlaygroundEvent.objects.filter(status="open").select_related(
        "Playground"
    )
    serializer_class = PlaygroundEventSerializer
    permission_classes = [
        permissions.IsAuthenticated,
    ]
    pagination_class = PlaygroundEventsPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["title"]
    ordering_fields = ["date"]
    ordering = ["date"]
