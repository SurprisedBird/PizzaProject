from dishes.models import Dishes, Ingredient
from django.forms import ModelForm

class AddDishForm(ModelForm):

	class Meta():
		model = Dishes
		fields = ['name', 'price']

class IngredientForm(ModelForm):

	class Meta():
		model = Ingredient
		fields = ['name', 'price']

class DishesForm(ModelForm):

	class Meta():
		model = Dishes
		fields = ['name', 'price', 'ingridients']