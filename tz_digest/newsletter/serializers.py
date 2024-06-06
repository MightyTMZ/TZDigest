from rest_framework import serializers
from .models import *


class NewsletterSerializer(serializers.Serializer):
    class Meta:
        model = Newsletter
        fields = [
            'name',
            'description',
            'created_at',
            'updated_at'
        ]


class NewsletterEditionSerializer(serializers.Serializer):
    newsletter = NewsletterSerializer()
    class Meta:
        model = NewsletterEdition
        fields = [
            'newsletter',
            'title',
            'content',
            'published_at',
            'created_at',
            'updated_at'
        ]

