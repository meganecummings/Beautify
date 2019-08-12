from django.urls import path
from . import views


urlpatterns = [
path('status', views.json_res, name='status'),
path('', views.home_view, name='home_view'),
path('looks/', views.looks_list, name='looks_list'),
path('items/', views.items_list, name='items_list'),
path('items/<int:pk>', views.view_item, name='view_item'),
path('order_view/', views.order_view, name='order_view'), 
path('about/', views.about, name='about'),
path('profile/', views.profile, name='profile')
# path('checkout/', views.checkout, name='checkout')
]