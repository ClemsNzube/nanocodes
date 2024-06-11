from rest_framework import serializers
from .models import Event, Category

class EventSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False,
        many=True,
        allow_null=True
    )

    class Meta:
        model = Event
        fields = '__all__'