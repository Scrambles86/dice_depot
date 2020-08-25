from django import forms
from .models import sellGame

class SaleForm(forms.ModelForm):
    class Meta:
        model = sellGame
        fields = [
            'game_name',
            'sealed',
            'condition',
        ]