from django.contrib import admin
from dishes.models import Size, Dish, Ingredient, Discount, Drink


class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    filter_horisontal = ('ingridients')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(Size)
admin.site.register(Dish, DishAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Discount)
admin.site.register(Drink)
