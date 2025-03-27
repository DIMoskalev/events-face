from rest_framework import serializers
from .models import Playground, PlaygroundEvent


class PlaygroundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Playground
        fields = "__all__"


class PlaygroundEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaygroundEvent
        fields = "__all__"
