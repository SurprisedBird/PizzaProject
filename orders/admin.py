from django.contrib import admin
from orders.models import Order


# Register your models here.
class OrderAdmin(admin.ModelAdmin):
	list_display = ['id', 'price', 'place_delivery']
	readonly_fields = ['price']

admin.site.register(Order, OrderAdmin)
