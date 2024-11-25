from django.db import models

from aitools.models import TimeStampedModel
from users.views import User

TTS_STATUS = [
    ("pending", "Pending"),
    ("processing", "Processing"),
    ("completed", "Completed"),
    ("failed", "Failed"),
]


class TTSConverter(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    audio_file = models.FileField(upload_to="audio_files/")
    status = models.CharField(max_length=255, choices=TTS_STATUS)
    request_id = models.CharField(max_length=255, null=True, blank=True)
