from django.urls import path
from . import views

path('status', views.json_res, name='status' )
path('', views.items, name='item_list')