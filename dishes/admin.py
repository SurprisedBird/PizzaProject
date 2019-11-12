from django.contrib import admin
from dishes.models import Size, Dishes, Ingredient, Discount, Drink

class DishAdmin(admin.ModelAdmin):
	list_display = ('name', 'price')
	filter_horisontal = ('ingridients')

class IngredientAdmin(admin.ModelAdmin):
	list_display = ('name', 'price')
	
# Register your models here.

admin.site.register(Size)
admin.site.register(Dishes, DishAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Discount)
admin.site.register(Drink)

