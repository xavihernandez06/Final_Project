from django.contrib import admin
from django.urls import path

from pokedex.models import TypeEffectiveness, PokemonType, Attack, Pokemon

admin.site.register(TypeEffectiveness)
admin.site.register(PokemonType)
admin.site.register(Attack)
admin.site.register(Pokemon)

urlpatterns = [
    path('admin/', admin.site.urls),

    # path("", HomePageListView.as_view(), name="home"),
]
