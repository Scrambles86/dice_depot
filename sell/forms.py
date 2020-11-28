from django import forms
from .models import Game


class SaleForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = [
            'game_name',
            'email',
            'game_description',
            'sealed',
            'condition',
        ]