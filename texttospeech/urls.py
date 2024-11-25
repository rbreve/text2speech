from django.urls import path

from .views import CreateTTSRequestView, TTSUserTextsView

urlpatterns = [
    path("request/", CreateTTSRequestView.as_view(), name="create-tts-request"),
    path("texts/", TTSUserTextsView.as_view(), name="list-tts-texts"),
]
