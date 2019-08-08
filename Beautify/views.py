from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *

# Create your views here.

def home(request):
  return HttpResponse("You are home")

def json_res(request):
  return JsonResponse({ "status" : "Ok" })

# Items
def items_list(request):
  items = Item.objects.all()
  return render(request, 'items_list.html', {"items": items})

# Looks
def looks_list(request):
  looks = Look.objects.all()
  return render(request, 'looks_list.html', {'looks': looks})


# Purchasing
def order_view(request):
  user = request.user
  order_items = OrderItem.objects.filter(user=user)
  return render(request, 'order_view.html', {'items': items})

# def checkout(request):


