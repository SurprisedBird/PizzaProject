from django.urls import path
from . import views
from dishes.models import Dishes

urlpatterns = [
	path('dishes/list/', views.DishesListView.as_view(), name="dishes_list"),
	path('ingredients/list/', views.IngredientsListView.as_view(), name="ingredients_list"),
	path('dishes/', views.DishesTamplateView.as_view()),
	path('dishes/', views.DishesTamplateView.as_view()),
]