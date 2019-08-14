from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib.auth.decorators import login_required


# Home
def home(request):
  return HttpResponse("We're home!")

def home_view(request):
  featured = Item.objects.all().filter(brand="Colourpop").filter(category="Eyes")
  return render(request, 'home_view.html', {'featured': featured})

def json_res(request):
  return JsonResponse({ "status" : "Ok" })

# Items
def items_list(request):
  items = Item.objects.all()
  return render(request, 'items_list.html', {'items': items})

def view_item(request, pk):
  item = Item.objects.get(id=pk)
  return render(request, 'view_item.html', {'item': item})

# Looks
def looks_list(request):
  items = Item.objects.filter(category='Looks')
  return render(request, 'items_list.html', {'items': items})

def view_look(request):
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
    # order_item.save()
      # redirect to order_view
    return redirect('order_view')
# else create order open
  else:
    # create order attached to user
    # order = Order.objects.get(user=user)
    item = Item.objects.get(pk=pk)
    user_order = Order.objects.create(user=user, quantity=0)
    # user_order.save()
    order_item = OrderItem.objects.create(order=user_order, item=item)
    # create order_item with new order2
    item = Item.objects.get(pk=pk)
    # item.quantity += 1
    user_order.save()
    # redirect to order_view
    # messages.success(request, f'You have successfully added { item.name } to your cart!')
    # print("Failed to add to cart")
    return redirect('order_view')

@login_required
def order_view(request):
  user = request.user
  orders = Order.objects.filter(user=user.pk)
  return render(request, 'order_view.html', {'orders': orders})

@login_required
def delete_item_from_order(request, pk):
  user = request.user
  item = OrderItem.objects.get(id=pk)
  order = Order.objects.get(user=user, purchased=False)
  order_item = OrderItem.objects.get(order=order, item=item)
  order_item.clear(item)
  return redirect('order_view')


@login_required
def profile(request):
  user = request.user
  return render(request, 'home_view.html')


# @login_required
# def checkout(request):
#   user = request.user
#   return render(request, 'profile.html' )
