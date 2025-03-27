from rest_framework import generics
from .models import PlaygroundEvent
from .serializers import PlaygroundEventSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from .paginators import PlaygroundEventsPaginator


class PlaygroundEventListView(generics.ListAPIView):
    queryset = PlaygroundEvent.objects.filter(status='open').select_related('Playground')
    serializer_class = PlaygroundEventSerializer
    pagination_class = PlaygroundEventsPaginator
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['title']
    ordering_fields = ['date']
    ordering = ['date']
