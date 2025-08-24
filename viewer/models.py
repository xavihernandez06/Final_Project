from django.db.models import Model, CharField, ForeignKey, DO_NOTHING, IntegerField, FloatField, DateField, TextField , CASCADE, SET_NULL

# Create your models here.

class TypeEffectiveness(Model):
    attack_type = ForeignKey(
        'PokemonType', 
        related_name='deals_effective_damage_to',
        on_delete=DO_NOTHING
    )
    defense_type = ForeignKey(
        'PokemonType', 
        related_name='takes_effective_damage_from',
        on_delete=DO_NOTHING
    )
    multiplier = FloatField()

    def __str__(self):
        return f"{self.attack_type.name} ➜ {self.defense_type.name}: x{self.multiplier}"

class PokemonType(Model):
    name = CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Attack(Model):
    name = CharField(max_length=50, unique=True)
    type = ForeignKey(PokemonType, on_delete=DO_NOTHING)
    power = IntegerField()

    def __str__(self):
        return f"{self.name} (Power: {self.power}, Type: {self.type})"

class Pokemon(Model):
    name = CharField(max_length=128, unique=True, primary_key=True)
    type_1 = ForeignKey(
        PokemonType, 
        related_name='primary_type_pokemons', 
        on_delete=SET_NULL
        )
    type_2 = ForeignKey(
        PokemonType, 
        related_name='secondary_type_pokemons', 
        on_delete=SET_NULL, 
        null=True, 
        blank=True
        )
    hp = IntegerField()
    attack = IntegerField()
    defense = IntegerField()
    description = TextField()
    attack_1 = ForeignKey(
        Attack, 
        related_name='attack1_pokemons', 
        on_delete=SET_NULL
        )
    attack_2 = ForeignKey(
        Attack, 
        related_name='attack1_pokemons', 
        on_delete=SET_NULL
        )