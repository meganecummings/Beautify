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
  order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
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
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

  def add_to_cart(request, item_id):
    user = request.user
    #if there is an open order attached to user
    if User.objects.filter(order=order).exists():
      # create order_item with order
      order_item = Order.objects.create(item=item)
    # else create order open
    else:
      # create order_item with new order

    item = Item.objects.get(pk=item_id)
    order_item = Order.objects.create(item=item)
    order = Order.objects.filter(user=request.user)
    order.quantity += 1
    order.save()
    messages.success(request, f'You have successfully added { item.name } to your cart!')

  def delete_from_cart(request, item_id):
    Item.objects.get(Item, pk=item_id).delete()
    return redirect('order_view') 

    
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