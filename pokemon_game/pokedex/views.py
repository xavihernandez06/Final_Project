from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from pokedex.models import StatusEffect, TypeEffectiveness, PokemonType, Attack, Pokemon

def home(request):
    return render(request, 'home_page.html')

def pokedex_view(request):
    pokemons = Pokemon.objects.all().order_by('name')
    return render(request, 'pokedex.html', {'pokemons': pokemons})

# # Functional View
# def home_page(request):
#     pokemon = Pokemon.objects.all()
#     return render(
#         request, 
#         template_name="home_page.html", 
#         context={"pokemon": pokemon}
#     )

# # CBV (Class-Based Views)
# class HomePage(TemplateView):
#     template_name = "home_page.html"
#     pokemon = Pokemon.objects.all()
#     extra_context = {"pokemon": pokemon}

# class HomePageListView(ListView):
#     template_name = "home_page.html"
#     model = Pokemon
