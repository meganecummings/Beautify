from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Order(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  date_created = models.DateTimeField(auto_now=False, auto_now_add=True)
  date_updated = models.DateTimeField(auto_now=True, auto_now_add=False)
  purchased = models.BooleanField(default=False)
  quantity = models.PositiveIntegerField()

class Item(models.Model):
  brand = models.CharField(max_length=30, blank=True, null=True)
  name = models.CharField(max_length=100, unique=True)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  sku = models.CharField(max_length=20)
  img = models.TextField()
  slug = models.SlugField(max_length=50, unique=True, editable=False)
  available = models.BooleanField(default=True)
  category = models.CharField(max_length=30, blank=True, null=True)
  color = models.CharField(max_length=30, blank=True, null=True)
  stock = models.PositiveIntegerField()

  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super(Item, self).save(*args, **kwargs)

class OrderItem(models.Model):
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')

class Look(models.Model):
  name = models.CharField(max_length=100, unique=True)
  img = models.TextField()
  description = models.CharField(max_length=250)
  category = models.CharField(max_length=30, blank=True, null=True)
  featured = models.BooleanField(default=False)
  video = models.TextField(blank=True, null=True)
  slug = models.SlugField(max_length=50, unique=True, editable=False)

  def __str__(self):
    return self.name

  def save(self, *args, **kwargs):
    self.slug = slugify(self.name)
    super(Look, self).save(*args, **kwargs)

class LookItem(models.Model):
  item = models.ForeignKey(Item, on_delete=models.CASCADE)
  look = models.ForeignKey(Look, on_delete=models.CASCADE)