# coding=utf-8
from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post


class PostSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('content',)


class PostUrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('url',)

