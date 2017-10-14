from django.db import models

# Create your models here.


class Type(models.Model):
    NORMAL = 'Normal'
    FIGHTING = 'Fighting'
    FLYING = 'Flying'
    POISON = 'Poison'
    GROUND = 'Ground'
    ROCK = 'Rock'
    BUG = 'Bug'
    GHOST = 'Ghost'
    STEEL = 'Steel'
    FIRE = 'Fire'
    WATER = 'Water'
    GRASS = 'Grass'
    ELECTRIC = 'Electric'
    PSYCHIC = 'Psychic'
    ICE = 'Ice'
    DRAGON = 'Dragon'
    DARK = 'Dark'
    FAIRY = 'Fairy'


    TYPE_CHOICES = (
        (NORMAL, 'Normal'),
        (FIGHTING, 'Fighting'),
        (FLYING, 'Flying'),
        (POISON, 'Poison'),
        (GROUND, 'Ground'),
        (ROCK, 'Rock'),
        (BUG, 'Bug'),
        (GHOST, 'Ghost'),
        (STEEL, 'Steel'),
        (FIRE, 'Fire'),
        (WATER, 'Water'),
        (GRASS, 'Grass'),
        (ELECTRIC, 'Electric'),
        (PSYCHIC, 'Psychic'),
        (ICE, 'Ice'),
        (DRAGON, 'Dragon'),
        (DARK, 'Dark'),
        (FAIRY, 'Fairy')
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, choices=TYPE_CHOICES, default=NORMAL)