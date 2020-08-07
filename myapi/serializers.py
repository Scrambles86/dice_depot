from rest_framework import serializers
from .models import Game

class GameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'name', 'publishers', 'year_published', 'max_players', 'image_url', 'msrp', 'price')