from django.contrib import admin
from django.urls import path, include

from pokedex.models import StatusEffect, TypeEffectiveness, PokemonType, Attack, Pokemon
from pokedex.views import home, pokedex_view, create_pokemon

from django.contrib.auth.views import LogoutView

admin.site.register(StatusEffect)
admin.site.register(TypeEffectiveness)
admin.site.register(PokemonType)
admin.site.register(Attack)
admin.site.register(Pokemon)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pokedex/', pokedex_view, name='pokedex'),
    path('', home, name='home'),
    path("create/", create_pokemon, name="create_pokemon"),
    path('accounts/logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),
]
