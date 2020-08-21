from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=60)
    primary_publisher = models.CharField(max_length=60)
    year_published = models.IntegerField()
    max_players = models.IntegerField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    msrp = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
