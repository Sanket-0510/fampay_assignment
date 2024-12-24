from django.contrib import admin
from .models import Video, APIKey

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'video_id', 'channel_id', 'publish_date_time', 'created', 'last_updated')
    list_filter = ('publish_date_time',)
    search_fields = ('title', 'description', 'video_id', 'channel_id')
    ordering = ('-publish_date_time',)

@admin.register(APIKey)
class APIKeyAdmin(admin.ModelAdmin):
    list_display = ('key', 'is_limit_over')
    list_filter = ('is_limit_over',)
    search_fields = ('key',)
