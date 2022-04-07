from rest_framework import serializers
from .models import *


class ImageResizerSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageResizer
        fields = '__all__'
