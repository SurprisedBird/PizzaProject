from django import forms
from dishes.models import Dish, Ingredient
from django.forms import ModelForm


class AddDishForm(ModelForm):

    class Meta():

        model = Dish
        fields = ['name', 'price']


class IngredientForm(ModelForm):

    class Meta():

        model = Ingredient
        fields = ['name', 'price']


class DishesForm(ModelForm):

    class Meta():

        model = Dish
        fields = ['name', 'price', 'ingridients']


class PizzaForm(forms.Form):
    pizza_id = forms.IntegerField()
    count = forms.IntegerField()
    size = forms.CharField()
