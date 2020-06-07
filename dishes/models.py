from django.db import models
from accounts.models import User


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


class Ingredient(BaseItem):

    def __str__(self):
        return self.name


class AbstractDish(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    size = models.ForeignKey(Size, blank=True, null=True,  on_delete=models.SET_NULL)
    discount = models.ForeignKey(Discount, blank=True, null=True, on_delete=models.SET_NULL)
    ingridients = models.ManyToManyField(Ingredient)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    model_picture = models.ImageField(upload_to='media/', null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ["pk"]

    def __unicode__(self):
        return self.__str__()


class Dish(BaseItem):
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)
    ingridients = models.ManyToManyField(Ingredient)

    class Meta:
        verbose_name_plural = 'Dish'

    def __str__(self):
        return self.name


class Drink(BaseItem):

    def __str__(self):
        return self.name


class InstanceDish(AbstractDish):
    dish = models.ForeignKey(Dish, related_name="dish_template", blank=True, null=True, on_delete=models.SET_NULL)
    count = models.IntegerField(default=0)


class Order(models.Model):
    dishes = models.ManyToManyField(InstanceDish, related_name="dishes", null=True, blank=True)
    user = models.ForeignKey(User, related_name="users", null=True, on_delete=models.SET_NULL)
    full_price = models.DecimalField(max_digits=6, decimal_places=2, default=0)

    def get_full_price(self):
        full_price = 0
        dishes = self.dishes.all()
        for dish in dishes:
            get_full_price += dish.price*dish.count
        print(full_price)
        return full_price

    def __str__(self):
        return str(self.full_price)
