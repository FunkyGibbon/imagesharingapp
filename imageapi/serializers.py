from rest_framework import serializers

from imageapi.models import Media

class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = 'id', 'caption', 'liked', 'image', 'dateuploaded'

