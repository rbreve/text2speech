import uuid
from texttospeech.models import TTSConverter
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from .models import TTSConverter

class TTSRequestSerializer(serializers.ModelSerializer):
    permission_classes = [IsAuthenticated] 

    text = serializers.CharField(required=True, min_length=2, max_length=5000, error_messages={
        "min_length": "Text must be at least 2 characters long.",
        "max_length": "Text must be at most 5000 characters long.",
    })
    
    class Meta:
        model = TTSConverter
        fields = ["id", "text"]
        read_only_fields = ["id", "status", "created_at"]


    def create(self, validated_data):
        user = self.context["request"].user

        #temporary request id this could be fetched from the converter process
        request_id = str(uuid.uuid4())

        tts_converter = TTSConverter.objects.create(user=user, text=validated_data["text"], status="pending", request_id=request_id)
        return tts_converter

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["status"] = instance.get_status_display()
        representation["request_id"] = instance.request_id
        return representation

class TTSUserTextsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TTSConverter
        fields = ["id", "text", "status", "created_at", "updated_at"]
        read_only_fields = ["id", "status", "created_at", "updated_at", "request_id"]
