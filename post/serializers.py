from rest_framework import serializers

from .models import Tweet, Reply


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["text", "image", "created_at", "updated_at"]


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ["text", "created_at", "updated_at"]
