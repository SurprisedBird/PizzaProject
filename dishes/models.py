from django.db import models

class Size(models.Model):
	SMALL = 1
	MIDDLE = 2
	BIG = 3
	SIZES = [
   	(SMALL, 60),
    (MIDDLE, 120),
   	(BIG, 180),
    ]

	name = models.CharField(max_length=50)
	size = models.IntegerField(choices=SIZES, default=0)
	
	def __str__(self):
		return self.name


class Discount(models.Model):
	type = models.CharField(max_length=30)
	amount = models.IntegerField()
	
	def __str__(self):
		return self.type

class BaseItem(models.Model):
	name = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	class Meta:
		abstract = True

class Ingredient(models.Model):
	name = models.CharField(max_length=50)
	price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	def __str__(self):
		return self.name

class Dishes(models.Model):
	name = models.CharField(max_length=50)
	size = models.ForeignKey(Size, on_delete=models.CASCADE)
	discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
	ingridients = models.ManyToManyField(Ingredient)
	price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	class Meta:
		verbose_name_plural = 'Dishes'

	def __str__(self):
		return self.name

class Drink(models.Model):
	name = models.CharField(max_length=50)
	prise = models.DecimalField(max_digits=6, decimal_places=2, default=0)

	def __str__(self):
		return self.name
		
		

		