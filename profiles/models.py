from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    """
    Model to store the order history and delivery data 
    for a user for repeat transactions
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
