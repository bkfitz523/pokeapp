from django.contrib import admin
from pokemon.models import Type, Region, Nature
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
