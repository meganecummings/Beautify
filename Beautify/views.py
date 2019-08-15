from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required
import decimal
import stripe
stripe.api_key = "sk_test_aKXivJtOPosLqtBi0GzFepuE00nUWZJb61"


# Home
def home(request):
  return HttpResponse("We're home!")

def home_view(request):
  featured = Item.objects.filter(brand="Colourpop").filter(category="Eyes")
  featured_looks = Item.objects.filter(category='Looks')
  return render(request, 'home_view.html', {'featured_looks': featured_looks, 'featured': featured})

def json_res(request):
  return JsonResponse({ "status" : "Ok" })

# Items
def items_list(request):
  items = Item.objects.all()
  return render(request, 'items_list.html', {'items': items})

def view_item(request, pk):
  item = Item.objects.get(id=pk)
  return render(request, 'view_item.html', {'item': item})

def slug_view(request, slug):
  item = Item.objects.get(slug=slug)
  return render(request, 'view_item.html', {'item': item}) 

# Looks
def looks_list(request):
  items = Item.objects.filter(category='Looks')
  return render(request, 'items_list.html', {'items': items})

def view_look(request, pk):
  item = Item.objects.get(id=pk)
  return render(request, 'view_item.html', {'item': item})

def about(request):
  return render(request, 'about.html')

# Purchasing
@login_required
def add_to_cart(request, pk):
  #if there is an open order attached to user
  user = request.user
  if Order.objects.filter(user=user).filter(purchased=False).exists():
    order = Order.objects.get(user=user)
    item = Item.objects.get(pk=pk)
  # create order_item with order
    order_item = OrderItem.objects.create(item=item, order=order)
      # redirect to order_view
    return redirect('order_view')
# else create order open
  else:
    # create order attached to user
    item = Item.objects.get(pk=pk)
    user_order = Order.objects.create(user=user, quantity=0)
    order_item = OrderItem.objects.create(order=user_order, item=item)
    # create order_item with new order2
    item = Item.objects.get(pk=pk)
    # redirect to order_view
    return redirect('order_view')

@login_required
def order_view(request):
  user = request.user

  # item = Item.objects.get(id=pk)
  # order_item = Order.objects.get(id=order_item)
  orders = Order.objects.filter(user=user.pk)
  # user_order = OrderItem.objects.filter(user=user)
  return render(request, 'order_view.html', {'orders': orders})
  orders = Order.objects.filter(user=user.pk).filter(purchased=False)
  for order in orders:
    all_items = order.items.all()
    total_price = sum(item.item.price for item in all_items)
    sales_tax = decimal.Decimal('0.0725')
    print(sales_tax)
    estimated_tax = (total_price*sales_tax)
    estimated_total = (total_price+estimated_tax)
    print(estimated_total)
    stripe_total = (estimated_total*100)

  return render(request, 'order_view.html', {'orders': orders, 'total_price': total_price, 'estimated_total': estimated_total, 'estimated_tax': estimated_tax, 'stripe_total': stripe_total })

@login_required
def delete_item_from_order(request, pk):
  order_item = OrderItem.objects.get(id=pk).delete()
  return redirect('order_view')


@login_required
def profile(request):
  user = request.user
  return render(request, 'home_view.html')


@login_required
def checkout(request):
  user = request.user
  return render(request, 'checkout.html' )

