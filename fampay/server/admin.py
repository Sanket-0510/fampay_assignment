from django.contrib import admin
from .models import Video, APIkey

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('video_title', 'video_id', 'channel_id','channel_title', 'video_description', 'pub_date', 'thumb_url','created_at', 'last_updated')
    list_filter = ('pub_date',)
    search_fields = ('video_title', 'video_description', 'video_id', 'channel_id')
    ordering = ('-pub_date',)

@admin.register(APIkey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'is_key_exhausted', 'created_at', 'updated_at')
    list_filter = ('is_key_exhausted',)
    search_fields = ('key',)
