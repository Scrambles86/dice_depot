from django.db import models

# Create your models here.

GAME_CONDITION = (
    ('perfect,', 'PERFECT'),
    ('good', 'GOOD'),
    ('well used', 'WELL USED'),
    ('damaged', 'DAMAGED'),
)


class Game(models.Model):

    game_name = models.CharField(max_length=254, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    game_description = models.TextField(max_length=512, null=True, blank=True)
    sealed = models.BooleanField(null=True)
    condition = models.CharField(max_length=25, choices=GAME_CONDITION, default='good')

    def __str__(self):
        return self.game_name
