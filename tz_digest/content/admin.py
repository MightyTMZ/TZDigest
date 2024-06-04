from django.contrib import admin
from .models import Article, TextBlock, HeadingBlock, ImageBlock


class TextBlockInline(admin.StackedInline):
    model = TextBlock
    extra = 1


class HeadingBlockInline(admin.StackedInline):
    model = HeadingBlock
    extra = 1


class ImageBlockInline(admin.StackedInline):
    model = ImageBlock
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'is_published', 'created_at', 'published_at')
    list_filter = ('is_published', 'created_at', 'published_at')
    search_fields = ('title', 'author__username')
    inlines = [TextBlockInline, HeadingBlockInline, ImageBlockInline]
