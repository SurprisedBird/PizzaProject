from django.db import models
from dishes.models import Dishes, Drink

# Create your models here.
class Order(models.Model):
	dishes = models.ManyToManyField(Dishes)
	drinks = models.ManyToManyField(Drink)
	date_created = models.DateTimeField(auto_now_add=True)
	price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
	place_delivery = models.CharField(max_length=250)
	user_profile = models.CharField(max_length=250)

	def save(self, *args, **kwards):
		price_dishes = sum([dishes.price for dish in self.dishes.all()])
		price_drinks = sum([drinks.price for drink in self.drinks.all()])
		print('price_dishes:', price_dishes)
		self.price = price_dishes + price_drinks
		super().save(*args, **kwards)
	
