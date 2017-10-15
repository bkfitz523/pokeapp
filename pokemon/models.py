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
    name = models.CharField(max_length=64, choices=TYPE_CHOICES, default=NORMAL)

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
    name = models.CharField(max_length=64, choices=REGION_CHOICES, default=KANTO)

    def __str__(self):
        return self.name


class Nature(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    increased_stat = models.CharField(max_length=50, blank=True)
    decreased_stat = models.CharField(max_length=50, blank=True)
    favorite_flavor = models.CharField(max_length=50, blank=True)
    disliked_flavor = models.CharField(max_length=50, blank=True)


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    type_primary = models.ForeignKey(Type, default=1, related_name='type_primary', on_delete=models.DO_NOTHING)
    type_secondary = models.ForeignKey(Type, default=0, related_name='type_secondary',
                                       on_delete=models.DO_NOTHING)
    region = models.ForeignKey(Region, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Move(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.ForeignKey(Type, default=1, on_delete=models.DO_NOTHING)
    category = models.CharField(max_length=50, default='Physical')
    contest = models.CharField(max_length=50, default='Cool')
    power = models.CharField(max_length=50, default='20')
    power_points = models.IntegerField()
    accuracy = models.CharField(max_length=50, default='100')


class Stat(models.Model):
    NONE = '-'
    HP = 'HP'
    ATTACK = 'Attack'
    DEFENSE = 'Defense'
    SPECIAL_ATTACK = 'Special Attack'
    SPECIAL_DEFENSE = 'Special Defense'
    SPEED = 'Speed'

    STAT_CHOICES = (
        (NONE, '-'),
        (HP, 'HP'),
        (ATTACK, 'Attack'),
        (DEFENSE, 'Defense'),
        (SPECIAL_ATTACK, 'Special Attack'),
        (SPECIAL_DEFENSE, 'Special Defense'),
        (SPEED, 'Speed')
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=64, choices=STAT_CHOICES, default=HP)

    def __str__(self):
        return self.name

# TODO: Flavor table
