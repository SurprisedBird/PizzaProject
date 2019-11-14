from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from dishes.models import Dishes, Drink, Discount, Size, Ingredient

# Create your views here.
class DishesListView(ListView):
	model = Dishes
	template_name = 'dishes_list.html'
	context_object_name = 'dishes'


class DishesTamplateView(TemplateView):
	template_name = 'dishes.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['name'] = Dishes.objects.all()
		return context
