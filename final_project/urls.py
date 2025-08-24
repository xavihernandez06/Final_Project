from django.contrib import admin
from django.urls import path

from viewer.views import HomePageListView
from viewer.models import TypeEffectiveness, PokemonType, Attack, Pokemon

admin.site.register(TypeEffectiveness)
admin.site.register(PokemonType)
admin.site.register(Attack)
admin.site.register(Pokemon)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Home
    path("", HomePageListView.as_view(), name="home"),
]


