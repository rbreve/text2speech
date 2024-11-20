from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializer import TTSRequestSerializer, TTSUserTextsSerializer
from .models import TTSConverter

class CreateTTSRequestView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TTSRequestSerializer

class TTSUserTextsView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TTSUserTextsSerializer

    def get_queryset(self):
        return TTSConverter.objects.filter(user=self.request.user)
