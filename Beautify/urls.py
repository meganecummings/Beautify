from django.urls import path
from . import views

urlpatterns = [
path('status', views.json_res, name='status'),
path('', views.looks_list, name='home_view'),
path('looks/', views.looks_list, name='looks_list'),
path('items/', views.items_list, name='items_list'),
path('order_view/', views.order_view, name='order_view')
# path('checkout/', views.checkout, name='checkout')
]