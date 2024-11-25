from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from texttospeech.models import TTSConverter
from users.views import User


class TTSRequestTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testi", password="testi")
        self.client.force_authenticate(user=self.user)

    def test_create_tts_request(self):
        url = reverse("create-tts-request")
        data = {"text": "Convert this text to speech"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TTSConverter.objects.count(), 1)
        self.assertEqual(response.data["status"], "Pending")
        self.assertNotEqual(response.data["id"], None)
        self.assertNotEqual(response.data["request_id"], "")
