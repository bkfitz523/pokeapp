from django.db import models

# Create your models here.


class Type(models.Model):
    NONE = '-'
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
        (NONE, '-'),
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
    name = models.CharField(max_length=31, choices=TYPE_CHOICES, default=NORMAL)

    def __str__(self):
        return self.name


class Region(models.Model):
    KANTO = 'Kanto'
    JOHTO = 'Johto'
    HOENN = 'Hoenn'
    SINNOH = 'Sinnoh'
    UNOVA = 'Unova'
    KALOS = 'Kalos'
    ALOLA = 'Alola'

    REGION_CHOICES = (
        (KANTO, 'Kanto'),
        (JOHTO, 'Johto'),
        (HOENN, 'Hoenn'),
        (SINNOH, 'Sinnoh'),
        (UNOVA, 'Unova'),
        (KALOS, 'Kalos'),
        (ALOLA, 'Alola')
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=31, choices=REGION_CHOICES, default=KANTO)

    def __str__(self):
        return self.name