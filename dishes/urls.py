from django.urls import path
from . import views
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
from dishes import views_api


urlpatterns = [
    path('', cache_page(10*10)(TemplateView.as_view(template_name="index.html"))),
    path('dishes/', views.DishesListView.as_view(), name='dishes_list'),


    path('ingredients/list/', views.IngredientsListView.as_view(), name="ingredients_list"),

    path('ingredients/<int:pk>/edit/', views.IngredientFormEddit.as_view()),
    path('dishes/<int:pk>/edit/', views.DishesFormEddit.as_view()),

    path('pizzas/', views.PizzaView.as_view()),
    path('add/pizza/', views.AddPizzaView.as_view()),

    path('get_pizzas_api/', views_api.PizzaAPIView.as_view(), name="pizzas_api")
]
