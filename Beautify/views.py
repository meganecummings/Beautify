from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *


# Home
def home(request):
  return HttpResponse("We're home!")

def home_view(request):
  return render(request, 'home_view.html')

def json_res(request):
  return JsonResponse({ "status" : "Ok" })

# Items
def items_list(request):
  items = Item.objects.all()
  return render(request, 'items_list.html', {"items": items})

def view_item(request, pk):
  item = Item.objects.get(id=pk)
  return render(request, 'view_item.html', {'item': item})

# Looks
def looks_list(request):
  looks = Look.objects.all()
  return render(request, 'looks_list.html', {'looks': looks})

def view_look(request):
  look = Look.objects.get(id=pk)
  return render(request, 'view_item.html', {'look': look})

def about(request):
  return render(request, 'about.html')

# Purchasing
  def add_to_cart(request, item_id):
    user = request.user
    #if there is an open order attached to user
    if Order.objects.filter(user=user).exists():
      order = Order.objects.get(user=user)
    # create order_item with order
      order_item = OrderItem.objects.create(item=item_id, order=order)
        order_item.save()
        # redirect to order_view
        return redirect('order_view', item=item_id)
    # else create order open
    else:
      # create order attached to user
      user_order = Order.objects.create(user=user, quantity=0)
      user_order.save()
      order_item = OrderItem.objects.create(order=order, item=item_id)
      # create order_item with new order2
        item = Item.objects.get(pk=item_id)
        item.quantity += 1
        order.save()
        redirect to order_view
        messages.success(request, f'You have successfully added { item.name } to your cart!')


def order_view(request):
  user = request.user
<<<<<<< HEAD
  orders = Order.objects.filter(user=user, purchased=False)
  
  return render(request, 'order_view.html', {'orders': orders, 'user': user})
=======
  # item = Item.objects.get(id=pk)
  # order_item = Order.objects.get(id=order_item)
  order = Order.objects.filter(user=user)
  return render(request, 'order_view.html', {'user': user, 'order': order})
>>>>>>> 24e7980bf628c3d3dc35646d6d877de4f8d07aeb

# def checkout(request):

def profile(request):
  user = request.user
  return render(request, 'profile.html')

