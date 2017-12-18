from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    image = models.ImageField(upload_to = 'recipe_images')
    title = models.CharField(max_length=200)
    prepare_time = models.CharField(max_length = 20, blank=True)
    portions = models.CharField(max_length = 20, blank=True)
    preview_text = models.CharField(max_length = 100, blank=True)
    ingredients = models.TextField()
    preperation = models.TextField(blank=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
