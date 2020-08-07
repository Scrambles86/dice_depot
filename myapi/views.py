from django.shortcuts import render

from rest_framework import viewsets

from .serializers import GameSerializer
from .models import Game

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all().order_by('name')
    serializer_class = GameSerializer
