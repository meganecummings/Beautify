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

def about(request):
  return render(request, 'about.html')

# Purchasing
def order_view(request):
  user = request.user
  orders = Order.objects.filter(user=user)
  return render(request, 'order_view.html', {'orders': orders, 'user': user})

# def checkout(request):

def profile(request):
  user = request.user
  return render(request, 'profile.html')

