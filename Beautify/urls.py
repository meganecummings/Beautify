from django.urls import path
from . import views

path('status', views.json_res, name='status' )
path('', views.home_view, name='home_view')
path('looks/', views.looks, name='looks_list')
path('items/', views.looks, name='items_list')
path('shopping_bag/', views.shopping_bag, name='shopping_bag')
path('checkout/', views.checkout, name='checkout')