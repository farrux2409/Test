from rest_framework import serializers

from app.models import Post, Book


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
