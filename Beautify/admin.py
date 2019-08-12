from django.contrib import admin
from .models import Item, Look, Order, LookItem, OrderItem
# Register your models here.
admin.site.register(Item)
admin.site.register(Look)
admin.site.register(Order)
admin.site.register(LookItem)
admin.site.register(OrderItem)
