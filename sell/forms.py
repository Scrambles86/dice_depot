from django import forms
from .models import Game


class SaleForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'game_name',
            'sealed',
            'condition',
        ]