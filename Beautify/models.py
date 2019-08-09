from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
  purchased = models.BooleanField(default=False)
  quantity = models.IntegerField()

class Item(models.Model):
  name = models.CharField(max_length=100, unique=True)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  sku = models.CharField(max_length=20)
  img = models.TextField()
  slug = models.SlugField(max_length=50)
  available = models.BooleanField(default=True)
  stock = models.PositiveIntegerField()
  video = models.TextField(blank=True, null=True)
  category = models.CharField(max_length=30, blank=True, null=True)
  color = models.CharField(max_length=30, blank=True, null=True)
  order = models.ForeignKey(Order, on_delete=models.CASCADE)

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

