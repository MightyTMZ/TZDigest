from django.db import models
from django.utils.text import slugify
from datetime import timedelta


# content: Manage articles, posts, and other content to be included in newsletters.


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_picture_url = models.CharField(max_length=2083, editable=False)

    def __str__(self) -> str:
        return f"{self.first_name} + {self.last_name}"


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(default="-", editable=False, max_length=250)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="articles")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    featured_image = models.ImageField(upload_to='articles/%Y/%m/%d/', blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.title} - by {self.author}"

    def save(self, *args, **kwargs):
        # Update the slug using the title when the article is saved
        self.slug = slugify(self.title)

        if self.updated_at - self.created_at < timedelta(minutes=10):
            self.updated_at = self.created_at
            super().save(update_fields=['updated_at'])

            # Django is very picky when it comes to datetime, so we must ensure that minute differences in \
            # creation/update is not a problem

        super().save(*args, **kwargs)

    def get_article_url(self):
        return f'/{self.created_at.date()}/{self.slug}/'

    class Meta:
        ordering = ["-created_at"]


class ContentBlock(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='content_blocks')
    order = models.PositiveIntegerField()

    class Meta:
        abstract = True
        ordering = ['order']


# when it inherits the ContentBlock, it inherits all the attributes (including the "article" foreign key)
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
class TextBlock(ContentBlock):
    content = models.TextField()
    type = "text block"

    def __str__(self):
        return f"{self.order} - {self.type} - {self.article}"


class HeadingBlock(ContentBlock):
    heading = models.CharField(max_length=255)
    type = "heading block"

    def __str__(self):
        return f"{self.order} - {self.type} - {self.article}"


class ImageBlock(ContentBlock):
    image = models.ImageField(upload_to='articles/images/%Y/%m/%d/')
    caption = models.CharField(max_length=1500, blank=True)
    type = 'image block'

    def __str__(self):
        return f"{self.order} - {self.type} - {self.article}"
