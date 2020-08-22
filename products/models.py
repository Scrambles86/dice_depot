from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=60)
    sku = models.CharField(max_length=254, null=True, blank=True)
    primary_publisher = models.CharField(max_length=60)
    description = models.CharField(max_length=1024, null=True, blank=True)
    description_preview = models.CharField(max_length=512, null=True, blank=True)
    year_published = models.IntegerField()
    min_age = models.IntegerField()
    min_players = models.IntegerField(default=0.0)
    max_players = models.IntegerField(default=0.0)
    min_playtime = models.IntegerField(default=0.0)
    max_playtime = models.IntegerField(default=0.0)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    thumb_url = models.URLField(max_length=1024, null=True, blank=True)
    url = models.URLField(max_length=1024, null=True, blank=True)
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    msrp = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
