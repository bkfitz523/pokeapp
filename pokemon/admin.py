from django.contrib import admin
from pokemon.models import Type, Region, Nature, Stat, Move
from pokemon.models import Pokemon

# Register your models here.


class TypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)

admin.site.register(Type, TypeAdmin)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    ordering = ('id',)

admin.site.register(Region, RegionAdmin)


class NatureAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'increased_stat',
        'decreased_stat',
        'favorite_flavor',
        'disliked_flavor'
    )
    ordering = ('id',)

admin.site.register(Nature, NatureAdmin)


class PokemonAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'type_primary',
        'type_secondary',
        'region'
    )
    ordering = ('id',)

admin.site.register(Pokemon, PokemonAdmin)


class MoveAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'type',
        'category',
        'contest',
        'power',
        'power_points',
        'accuracy'
    )

admin.site.register(Move, MoveAdmin)


class StatAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'symbol')
    ordering = ('id',)

admin.site.register(Stat, StatAdmin)
