from django.contrib import admin
from django.urls import path

from pokedex.models import AttackEffect, TypeEffectiveness, PokemonType, Attack, Pokemon

admin.site.register(AttackEffect)
admin.site.register(TypeEffectiveness)
admin.site.register(PokemonType)
admin.site.register(Attack)
admin.site.register(Pokemon)

urlpatterns = [
    path('admin/', admin.site.urls),

    # path("", HomePageListView.as_view(), name="home"),
]
