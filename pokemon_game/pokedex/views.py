from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from pokedex.models import StatusEffect, TypeEffectiveness, PokemonType, Attack, Pokemon
from pokedex.forms import PokemonForm

def home(request):
    return render(request, 'home_page.html')

def pokedex_view(request):
    pokemons = Pokemon.objects.all().order_by('name')
    return render(request, 'pokedex.html', {'pokemons': pokemons})

def create_pokemon(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("pokemon_list")
    else:
        form = PokemonForm()
    return render(request, "create_pokemon.html", {"form": form})
