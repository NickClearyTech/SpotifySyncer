import django.contrib.auth
from django.db import models

# Create your models here.

class SpotifyKey(models.Model):

    user = models.OneToOneField(
        django.contrib.auth.get_user_model(),
        on_delete=models.DO_NOTHING(),
        related_name="spotify_keys"
    )
    refresh_key = models.BinaryField()
