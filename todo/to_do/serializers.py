from rest_framework import serializers
from .models import Board, TodoList

class BoardListAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'

class BoardCreateAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'


class TodoListAPIViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = "__all__"