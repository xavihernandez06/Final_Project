from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = [
            "name",
            "region",
            "type_1",
            "type_2",
            "hp",
            "attack",
            "defense",
            "speed",
            "description",
            "attack_1",
            "attack_2",
        ]