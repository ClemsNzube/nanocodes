from rest_framework import serializers
from .models import Event, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class EventSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        required=False,
        many=True,
        allow_null=True
    )
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Event
        fields = '__all__'
