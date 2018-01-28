from django.contrib import admin

# Register your models here.

# Import models below
from collection.models import Type, Region


# Setup
class TypeAdmin(admin.ModelAdmin):
    model = Type
    list_display = ('id', 'name',)
    readonly_fields = ('id', 'name')
    ordering = ('id',)


class RegionAdmin(admin.ModelAdmin):
    model = Region
    list_display = ('id', 'name',)
    readonly_fields = ('id', 'name')
    ordering = ('id',)

# Register models
admin.site.register(Type, TypeAdmin)
admin.site.register(Region, RegionAdmin)
