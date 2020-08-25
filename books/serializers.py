from rest_framework import serializers

from books.models import Book


class AddSetSerializer(serializers.Serializer):
    q = serializers.CharField(max_length=256)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
