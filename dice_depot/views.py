from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.models import APIKey
from rest_framework_api_key.permissions import HasAPIKey

# Lists all games or create new entry in admin
class GameList(APIView):

    def get(self, request):
        games = Games.objects.all()
        pass

    def post(self):
        pass