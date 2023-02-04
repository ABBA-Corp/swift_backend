from django.contrib import admin
from .models import *


@admin.register(VisaCategory)
class VisaCategoryAdmin(admin.ModelAdmin):
    list_display = ["country"]


@admin.register(BuisnessCategory)
class BuisnessCategoryAdmin(admin.ModelAdmin):
    list_display = ["country"]


admin.site.register(CitizenCategory)
admin.site.register(Travel)
admin.site.register(Images)
admin.site.register(News)
admin.site.register(Unnecessary)
admin.site.register(HeaderSlider)


@admin.register(DityoSlider)
class DityoSliderAdmin(admin.ModelAdmin):
    list_display = ["name_uz", "price"]


@admin.register(CountrySlider)
class CountrySliderAdmin(admin.ModelAdmin):
    list_display = ["name_uz"]


@admin.register(Countries)
class CountriesAdmin(admin.ModelAdmin):
    list_display = ["name_uz"]


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = ["name_uz"]


@admin.register(Flag)
class FlagAdmin(admin.ModelAdmin):
    list_display = ["name_uz"]