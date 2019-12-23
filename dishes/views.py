from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, FormView
from dishes.models import Dish, Drink, Discount, Size, Ingredient, Order, InstanceDish
from dishes.forms import IngredientForm, DishesForm, PizzaForm
from accounts.models import User
from django.core.cache import cache


class DishesListView(ListView):
    model = Dish
    template_name = 'dishes_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cache.set('client_ip', self.request.META['REMOTE_ADDR'], 60*2)
        current_client_ip = self.request.META['REMOTE_ADDR']
        if current_client_ip != cache.get('client_ip'):
            print("Error: Your IP was changed from {} to {}".format(cache.get('client_ip'), current_client_ip))

        context['count'] = Dish.objects.all().count()
        context['filter'] = Dish.objects.filter(price__gt=40).values_list("name")
        context['name_list'] = Dish.objects.all().values_list("name")
        return context


class IngredientsListView(ListView):
    model = Ingredient
    template_name = 'ingredients_list.html'
    context_object_name = 'ingredients'


class DishesTamplateView(TemplateView):
    template_name = 'dishes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = Dish.objects.all()
        return context


class IngredientFormEddit(UpdateView):
    form_class = IngredientForm
    model = Ingredient
    success_url = "/ingredients/list"
    template_name = 'ingredients_form.html'


class DishesFormEddit(UpdateView):
    form_class = DishesForm
    model = Dish
    success_url = "/dishes/list"
    template_name = 'dishes_form.html'


class PizzaView(FormView):
    template_name = "pizza.html"
    form_class = PizzaForm
    success_url = "pizzas/"

    def get_context_data(self, **kwargs):
        context = super(PizzaView, self).get_context_data(**kwargs)
        context['pizzas'] = Dish.objects.all()
        print(context['pizzas'])
        return context


class AddPizzaView(FormView):
    template_name = "add_pizza.html"
    form_class = PizzaForm
    success_url = "/add/pizza/"

    def get_context_data(self, **kwargs):
        context = super(AddPizzaView, self).get_context_data(**kwargs)
        context['pizzas'] = InstanceDish.objects.distinct()
        context['order'] = Order.objects.first()
        return context

    def form_valid(self, form):
        dish_id = form.cleaned_data.get('pizza_id')
        dish = Dish.objects.get(id=dish_id)
        dish_size = form.cleaned_data.get('size')
        size = Size.objects.get(name=dish_size)
        count = form.cleaned_data.get('count')
        instance_pizza = dish.create_instance_dish(count, size)
        order, created = Order.objects.get_or_create(user=self.request.user)
        order.dishes.add(instance_pizza)
        return super().form_valid(form)
