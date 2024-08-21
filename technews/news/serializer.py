from .models import News, Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']


class NewsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = News
        fields = ("__all__")

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        news = News.objects.create(**validated_data)

        # Handle tags
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            news.tags.add(tag)

        return news
