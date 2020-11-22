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
    model_pic = models.ImageField(upload_to = 'user_game_images/', default = '')
    sealed = models.BooleanField(help_text="Only tick this box if your game is still contained in it's original wrapping")
    condition = models.CharField(max_length=25, choices=GAME_CONDITION, default='good')

    def __str__(self):
        return self.game_name
