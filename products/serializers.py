from .models import Book
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response

User = get_user_model()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'owner', 'owner_card', 'info', 'price', 'sale']
        read_only_fields = ('id', 'owner', 'owner_card')

    def create(self, validated_data):
        return Book.objects.create(owner=self.context['user'], **validated_data)
