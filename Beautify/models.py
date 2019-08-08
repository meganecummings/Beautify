from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
  name = models.CharField(max_length=100, unique=True)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  sku = models.CharField(max_length=20)
  img = models.TextField()
  slug = models.SlugField(max_length=50)
  available = models.BooleanField(default=True)
  stock = models.IntegerField()
  video = models.TextField(blank=True, null=True)

  def __str__(self):
    return self.name

class Look(models.Model):
  name = models.CharField(max_length=100)
  img = models.TextField()
  description = models.CharField(max_length=250)
  slug = models.SlugField(max_length=50)
  featured = models.BooleanField(default=False)

  
  def __str__(self):
    return self.name

class LookItem(models.Model):
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  look = models.ForeignKey(Look, on_delete=models.CASCADE)
  


class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
  purchased = models.BooleanField(default=False)
  

class OrderItem(models.Model):
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  quantity = models.IntegerField()
  def update_stock():
    return f"Item.stock - OrderItem.quantity"



