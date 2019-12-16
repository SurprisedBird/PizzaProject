from django.views.generic.list import ListView
from django.views.generic import TemplateView
from dishes.models import Dishes, Ingredient
from django.views.generic.edit import UpdateView, FormView
from dishes.forms import IngredientForm, DishesForm

# Create your views here.
class DishesListView(ListView):
	model = Dishes
	template_name = 'dishes_list.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		cache.set('client_ip', self.request.META['REMOTE_ADDR'], 60*2)
		current_client_ip = self.request.META['REMOTE_ADDR']
		if current_client_ip != cache.get('client_ip'):
			print("Error: Your IP was changed from {} to {}".format(cache.get('client_ip'), current_client_ip))
		
		context['count'] = Dishes.objects.all().count()
		context['filter'] = Dishes.objects.filter(price__gt=40).values_list("name")
		context['name_list'] = Dishes.objects.all().values_list("name")
		return context

class IngredientsListView(ListView):
	model = Ingredient
	template_name = 'ingredients_list.html'
	context_object_name = 'ingredients'

class DishesTamplateView(TemplateView):
	template_name = 'dishes.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['name'] = Dishes.objects.all()
		return context

class IngredientFormEddit(UpdateView):
	form_class = IngredientForm
	model = Ingredient
	success_url = "/ingredients/list"
	template_name = 'ingredients_form.html'

class DishesFormEddit(UpdateView):
	form_class = DishesForm
	model = Dishes
	success_url = "/dishes/list"
	template_name = 'dishes_form.html'