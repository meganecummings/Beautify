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

  def __str__(self):
    return '{0} - {1}'.format(self.user, self.pk)

class Item(models.Model):
  brand = models.CharField(max_length=30, blank=True, null=True)
  name = models.CharField(max_length=100, unique=True)
  price = models.DecimalField(max_digits=5, decimal_places=2)
  sku = models.CharField(max_length=20)
  img = models.TextField()
  description = models.CharField(max_length=250, null=True)
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
  order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')


  # def add_to_cart(request, pk):
  #   user = request.user
  #   # Based on the user who is making the request, grab the cart object
  #   user_order = Order.objects.get_or_create(user=user)
  #   order_item = Item.objects.get(pk=item.pk)
  #   # Get entries in the cart
  #   user_order_item = OrderItem(item=item, user_order=user_order, quantity=0)
  #   # Get a list of your products
  #   items = Item.objects.all()

  #   if request.POST:
  #       # Get the product's ID from the POST request.
  #       item_id = request.POST.get(pk=item.pk)
  #       # Get the object using our unique primary key
  #       item_obj = Product.objects.get(pk=item.pk)
  #       # Get the quantity of the product desired.
  #       item_quantity = request.POST.get('order_quantity')
  #       # Create the new Entry...this will update the cart on creation
  #       Order.objects.create(order=order, item=item, quantity=quantity)
  #       return HttpResponse('order_view.html')

  #   return render(request, 'order_view.html', {'cart': cart, 'order_item': order_item, 'item': item})

  # def delete_from_cart(request, item_id):
  #   Item.objects.get(Item, pk=item_id).delete()
  #   return redirect('order_view') 

    

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