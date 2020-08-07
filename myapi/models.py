from django.db import models

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=60)
    publishers = models.CharField(max_length=60)
    year_published = models.IntegerField(max_length=4)
    max_players = models.IntegerField(max_length=4)
    image_url = models.ImageField(upload_to"static/images")
    msrp = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    price = models.DecimalField(max_digits=6, decimal_places=2)
