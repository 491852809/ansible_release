from rest_framework import serializers
from .models import *

class MusicSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='*',read_only=True)

    class Meta:
        model = Music
        fields = ('username','music_file','music_img','user')
