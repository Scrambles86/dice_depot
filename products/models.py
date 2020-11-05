from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=60)
    sku = models.CharField(max_length=254, null=True, blank=True)
    primary_publisher = models.CharField(max_length=60)
    description = models.CharField(max_length=1024, null=True, blank=True)
    description_preview = models.CharField(max_length=512, null=True, blank=True)
    year_published = models.IntegerField()
    players = models.ForeignKey('Players')
    age = models.ForeignKey('Age')
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    thumb_url = models.URLField(max_length=1024, null=True, blank=True)
    url = models.URLField(max_length=1024, null=True, blank=True)
    discount = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    msrp = models.DecimalField(max_digits=6, decimal_places=2, default=0.0)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class Players(models.Model):
    min_players = models.IntegerField(default=0.0)
    max_players = models.IntegerField(default=0.0)

    def __str__(self):
        return "%s %s" % (self.min_players, self.max_players)

class Age(models.Model):
    min_age = models.IntegerField()

    def __str__(self):
        return self.min_age
