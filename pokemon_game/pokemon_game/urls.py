from django.contrib import admin
from django.urls import path, include

from pokedex.models import StatusEffect, TypeEffectiveness, PokemonType, Attack, Pokemon
from pokedex.views import pokedex_view

admin.site.register(StatusEffect)
admin.site.register(TypeEffectiveness)
admin.site.register(PokemonType)
admin.site.register(Attack)
admin.site.register(Pokemon)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pokedex_view, name='pokedex')
]
