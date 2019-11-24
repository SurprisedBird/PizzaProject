from dishes.models import Dishes, Ingredient
from django.forms import ModelForm

class AddDishForm(ModelForm):

	class Meta():
		model = Dishes
		fields = ['name', 'price']