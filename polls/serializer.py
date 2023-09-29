from rest_framework import serializers
from .models import AuthorModel, BookModel,CategoryModel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=AuthorModel
        fields=(
            "id",
            "name",
            "surname",
            "date_of_birth",
            "date_of_death",
            "alive"
        )

class AuthorSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model=AuthorModel
        fields=(
            "id",
            "name",
            "surname",
            "date_of_birth",
            "date_of_death",
            "alive",
            "description"
        )
class AuthorSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model=AuthorModel
        fields=("__all__")

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookModel
        fields=(
            "id",
            "name",
            "author"
            )
        
class BookSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model=BookModel
        fields=(
            "id",
            "name",
            "page",
            "year_of_invented",
            "price",
            "description",
            "author"
            )
class BookSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model=BookModel
        fields=("__all__")
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=CategoryModel
        fields=(
            "id",
            "name"
        )