from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  sku = models.CharField(max_length=20)
  img = models.TextField()
  slug = models.SlugField(max_length=50)
  available = models.BooleanField(default=True)
  featured = models.BooleanField(default=False)
  stock = models.IntegerField(max_length=3)
  video = models.TextField(blank=True, null=True)

  def __str__(self):
    self.name

class Look(models.Model):
  name = models.CharField(max_length=100)
  img = models.TextField()
  description = models.CharField(max_length=250)
  slug = models.SlugField(max_length=50)
  
  def __str__(self):
    self.name




class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
  purchased = models.BooleanField(default=False)
  

class OrderItem(models.Model):
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  order = models.ForeignKey(Order, on_delete=models.CASCADE)
  quantity = models.IntegerField(max_length=3)
  def update_stock():
    return f"Item.stock - OrderItem.quantity"



