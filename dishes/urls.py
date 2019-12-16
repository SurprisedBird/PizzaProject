from django.urls import path
from . import views
from dishes.models import Dishes

urlpatterns = [
	path('', cache_page(10*10) (TemplateView.as_view(template_name="index.html"))),
	path('dishes/list/', views.DishesListView.as_view(), name="dishes_list"),
	path('ingredients/list/', views.IngredientsListView.as_view(), name="ingredients_list"),
	path('dishes/', views.DishesTamplateView.as_view()),
	path('dishes/', views.DishesTamplateView.as_view()),
	path('ingredients/<int:pk>/edit/', views.IngredientFormEddit.as_view()),
	path('dishes/<int:pk>/edit/', views.DishesFormEddit.as_view()),

]