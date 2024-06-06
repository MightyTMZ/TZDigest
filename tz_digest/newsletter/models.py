from django.db import models
from users.models import CustomUser

# FUCK WHAT THEY SAY!! YOUR NEWSLETTER IS OFFICIAL!!!!

class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.email

# a polymorphic example of a subscriber being a user
# all subscribers are users
# but not all users are subscribers --> users can "exist" in different forms

class Newsletter(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class NewsletterEdition(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    published_at = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.newsletter.name} - {self.title}"


class ScheduledNewsletter(models.Model):
    edition = models.ForeignKey(NewsletterEdition, on_delete=models.CASCADE)
    scheduled_at = models.DateTimeField()
    is_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Scheduled {self.edition.newsletter.name} - {self.edition.title} at {self.scheduled_at}"


class TextBlock(models.Model):
    edition = models.ForeignKey(NewsletterEdition, on_delete=models.CASCADE, related_name='text_blocks')
    content = models.TextField()
    type = models.CharField(max_length=50, default="text block")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.order} - {self.type} - {self.edition}"


class HeadingBlock(models.Model):
    edition = models.ForeignKey(NewsletterEdition, on_delete=models.CASCADE, related_name='heading_blocks')
    heading = models.CharField(max_length=255)
    type = models.CharField(max_length=50, default="heading block")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.order} - {self.type} - {self.edition}"


class ImageBlock(models.Model):
    edition = models.ForeignKey(NewsletterEdition, on_delete=models.CASCADE, related_name='image_blocks')
    image = models.ImageField(upload_to='newsletters/images/%Y/%m/%d/')
    caption = models.CharField(max_length=1500, blank=True)
    type = models.CharField(max_length=50, default="image block")
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.order} - {self.type} - {self.edition}"
