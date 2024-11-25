from django.urls import path

from .views import CreateTTSRequestView, TTSDeleteView, TTSUserTextsView

urlpatterns = [
    path("request/", CreateTTSRequestView.as_view(), name="create-tts-request"),
    path("texts/", TTSUserTextsView.as_view(), name="list-tts-texts"),
    path("texts/<int:pk>/delete/", TTSDeleteView.as_view(), name="tts-delete"),
]
