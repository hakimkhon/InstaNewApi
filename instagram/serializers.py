from rest_framework import serializers
from .models import Story, Profile

class StorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ('id', 'profile', 'media', 'created')

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'username')