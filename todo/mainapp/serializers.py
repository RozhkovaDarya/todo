from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Article, User, Notes


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class NotesSerializerBase(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'

        
class NotesSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Notes
        fields = '__all__'
