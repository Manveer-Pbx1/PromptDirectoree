from rest_framework import serializers

class PromptSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()