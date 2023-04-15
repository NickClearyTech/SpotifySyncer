import django.contrib.auth
from django.db import models


class SpotifyKey(models.Model):
    user = models.OneToOneField(
        django.contrib.auth.get_user_model(),
        on_delete=models.DO_NOTHING,
        related_name="spotify_keys",
        null=False,
    )
    refresh_key = models.BinaryField(null=False)
    expires = models.DateTimeField(null=False)
