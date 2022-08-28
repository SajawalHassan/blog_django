import uuid
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import uuid
from datetime import datetime, date

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now=True)

    class Meta:
        ordering = ['-createdAt', '-updatedAt']

    def __str__(self):
        return f"{str(self.title)} | {str(self.author)}"

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.id})
