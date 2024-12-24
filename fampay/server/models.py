from django.db import models

# Create your models here.
class Video(models.Model):
    channel_id = models.CharField(max_length=255, default=None)
    channel_title = models.CharField(max_length=255, default=None)
    video_id = models.CharField(max_length=255, default=None)
    video_title = models.CharField(max_length=255, default=None)
    video_description = models.CharField(max_length=255, default=None)
    pub_date = models.DateTimeField()
    thumb_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    
    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
    def __str__(self):
        return self.title


class APIkey(models.Model):
    key = models.TextField()
    is_key_exhausted = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)     

    class Meta:
        verbose_name = 'APIkey'
        verbose_name_plural = 'APIkeys'

    def __str__(self):
        return self.key  