from rest_framework import generics, permissions
from to_do.serializers import BoardCreateAPIViewSerializer, BoardListAPIViewSerializer
from to_do.models import Board
from django.db.models import Count
from django.shortcuts import render

class BoardListAPIView(generics.ListAPIView):
    serializer_class = BoardListAPIViewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Board.objects.annotate(count=Count('todolist__board'))
        return queryset
    

class BoardCreateAPIView(generics.CreateAPIView):
    serializer_class = BoardCreateAPIViewSerializer
    permission_classes = [permissions.IsAdminUser]


class BoardUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BoardCreateAPIViewSerializer
    permission_classes = [permissions.IsAdminUser]
    queryset = Board.objects.all()