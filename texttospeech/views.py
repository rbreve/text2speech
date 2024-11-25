from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from .models import TTSConverter
from .serializer import TTSRequestSerializer, TTSUserTextsSerializer


class CreateTTSRequestView(generics.CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TTSRequestSerializer


class TTSUserTextsView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TTSUserTextsSerializer

    def get_queryset(self):
        return TTSConverter.objects.filter(user=self.request.user)


class TTSCheckStatusView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TTSConverter.objects.filter(user=self.request.user)

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise NotFound("Not found")
        return obj


class TTSDeleteView(generics.DestroyAPIView):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TTSConverter.objects.filter(user=self.request.user)

    def get_object(self):
        obj = super().get_object()
        if obj.user != self.request.user:
            raise NotFound("Not found")
        return obj
