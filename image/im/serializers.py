from rest_framework import serializers
from .models import ImageModel


class ImageSerializer(serializers.ModelSerializer):
    """图片的序列化器"""
    class Meta:
        model = ImageModel
        fields = ['image']
