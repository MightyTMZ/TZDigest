from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            "first_name", 
            "last_name", 
            "profile_picture_url"
        ]

class TextBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextBlock
        fields = [
            "content", 
            'type', 
            'order',
        ]

class HeadingBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeadingBlock
        fields = [
            "heading", 
            'type', 
            'order',
        ]

class ImageBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageBlock
        fields = [
            "image", 
            'caption',
            'type', 
            'order',
        ]

class ArticleSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()  # Use AuthorSerializer as a nested serializer
    text_blocks = TextBlockSerializer(many=True, read_only=True)
    heading_blocks = HeadingBlockSerializer(many=True, read_only=True)
    image_blocks = ImageBlockSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        fields = ["title", 
                  "slug", 
                  'author', 
                  'created_at', 
                  'updated_at', 
                  'is_published', 
                  'featured_image',
                  'text_blocks', 
                  'heading_blocks', 
                  'image_blocks' 
                  ]