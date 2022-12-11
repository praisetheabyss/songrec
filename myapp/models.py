from django.db import models
import uuid
# from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

# Create your models here.
# class User(AbstractUser):
#     user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     email = models.EmailField()
#     birth_date = models.DateField()

#     def __str__(self):
#         return self.username

class Genre(models.Model):
    genre_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    genre_name = models.CharField(max_length=20)

    def __str__(self):
        return self.genre_name

class Music(models.Model):
    music_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    music_name = models.CharField(max_length=100)
    artist_name = models.CharField(max_length=100)
    album_name = models.CharField(max_length=100)
    last_reccomended = models.DateField(auto_now=True)

    def __str__(self):
        return self.music_name

# Forum

class Post(models.Model):
    post_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_title = models.CharField(max_length=200)
    post_text = models.TextField()
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.post_title

    # foreign key what_is_about(genero, artista, musica), e do user

class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    comment_text = models.TextField()
    created_at = models.DateField(auto_now=True)

    # foreign key do post e do user




