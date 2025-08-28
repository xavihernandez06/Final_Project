import json
from django.core.management.base import BaseCommand
from pokedex.models import Pokemon, PokemonType, Attack, StatusEffect, TypeEffectiveness

class Command(BaseCommand):
    help = 'Load Pokemon data from JSON file'

    def handle(self, *args, **kwargs):
        with open('pokemon_data.json') as f:
            data = json.load(f)
    
        for entry in data:
            # Get or create the types
            type_1_obj, _ = PokemonType.objects.get_or_create(name=entry["type_1"])
            type_2_name = entry.get("type_2")
            type_2_obj = None
            if type_2_name:
                type_2_obj, _ = PokemonType.objects.get_or_create(name=type_2_name)

            # Get or create attacks
            attack_1_obj, _ = Attack.objects.get_or_create(name=entry["attack_1"], defaults={"type": type_1_obj, "power": 50, "priority": 0.5})
            attack_2_obj, _ = Attack.objects.get_or_create(name=entry["attack_2"], defaults={"type": type_1_obj, "power": 50, "priority": 0.5})

            # Create the Pokemon
            pokemon, created = Pokemon.objects.get_or_create(
                name=entry["name"],
                defaults={
                    "region": entry.get("region", "Kanto"),
                    "type_1": type_1_obj,
                    "type_2": type_2_obj,
                    "hp": entry["hp"],
                    "attack": entry["attack"],
                    "defense": entry["defense"],
                    "speed": entry["speed"],
                    "description": entry["description"],
                    "attack_1": attack_1_obj,
                    "attack_2": attack_2_obj,
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created Pokemon: {pokemon.name}"))
            else:
                self.stdout.write(self.style.WARNING(f"Pokemon {pokemon.name} already exists"))