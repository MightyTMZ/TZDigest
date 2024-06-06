from django.contrib import admin
from .models import *


class TextBlockInline(admin.StackedInline):
    model = TextBlock
    extra = 1


class HeadingBlockInline(admin.StackedInline):
    model = HeadingBlock
    extra = 1


class ImageBlockInline(admin.StackedInline):
    model = ImageBlock
    extra = 1


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        'description',
        'created_at',
        'updated_at'
    ]

    search_fields = ['name', 'description']


@admin.register(NewsletterEdition)
class NewsletterEditionAdmin(admin.ModelAdmin):
    list_display = [
        'newsletter',
        'title',
        'published_at',
        'created_at',
        'updated_at'
    ]

    list_editable = [
        'title',
    ]

    search_fields = ['title', 'content']

    inlines = [TextBlockInline, HeadingBlockInline, ImageBlockInline]


class ScheduledNewsletterAdmin(admin.ModelAdmin):
    list_display = [
        'edition',
        'scheduled_at',
        'is_sent',
        'created_at'
    ]

    list_editable = [
        'scheduled_at'
    ]






