from django.db import models
from users.models import User

# Create your models here.
class VideoFavorito(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_id = models.CharField(max_length=100)
    titulo = models.CharField(max_length=255)
    thumbnail_url = models.URLField()

    def __str__(self):
        return f"{self.titulo} ({self.user.username})"
