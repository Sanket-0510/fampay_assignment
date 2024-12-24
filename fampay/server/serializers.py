from rest_framework import serializers
from .models import APIkey, Video

class APIKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = APIkey
        fields = ['id', 'key', 'is_active', 'is_limit_over', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = [
            'video_id', 'video_title', 'video_description', 'pub_date', 
            'channel_id', 'channel_title', 'thumb_url'
        ]
