from django.shortcuts import render
from django.views.generic import TemplateView, ListView, FormView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from viewer.models import TypeEffectiveness, PokemonType, Attack, Pokemon

# Functional View
def home_page(request):
    pokemon = Pokemon.objects.all()
    return render(
        request, 
        template_name="home_page.html", 
        context={"pokemon": pokemon}
    )

# CBV (Class-Based Views)
class HomePage(TemplateView):
    template_name = "home_page.html"
    pokemon = Pokemon.objects.all()
    extra_context = {"pokemon": pokemon}

class HomePageListView(ListView):
    template_name = "home_page.html"
    model = Pokemon
