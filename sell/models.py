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
    sealed = models.BooleanField(null=True)
    condition = models.CharField(max_length=25, choices=GAME_CONDITION, default='good')
    game_description = models.TextField(max_length=512, default="Please disclose any damage, defects, and/or missing pieces", null=True, blank=True)

    def __str__(self):
        return self.game_name
