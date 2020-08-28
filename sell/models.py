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
    sealed = models.BooleanField(label="Tick if sealed", help_text="Only tick this box if your game is still contained in it's original wrapping")
    condition = models.CharField(max_length=8, option=GAME_CONDITION, default='good')
