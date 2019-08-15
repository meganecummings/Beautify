from django.urls import path
from . import views


urlpatterns = [
path('status', views.json_res, name='status'),
path('', views.home_view, name='home_view'),
path('looks/', views.looks_list, name='looks_list'),
path('looks/<int:pk>', views.view_look, name='view_look'),
path('items/', views.items_list, name='items_list'),
path('items/<int:pk>', views.view_item, name='view_item'),
path('order_view/', views.order_view, name='order_view'), 
path('items/add/<int:pk>', views.add_to_cart, name='add_to_cart'), 
path('about/', views.about, name='about'),
# path('profile/', views.profile, name='profile'),
path('checkout/', views.checkout, name='checkout')
]

# in jinja, use set to create a function that will loop & add quantity times price to get subtotal
# once order is going to be purhased "place order" to set the purchased to 'true"