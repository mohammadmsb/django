from django.urls import path
from . import views
from .models import *
urlpatterns=[
    path('', views.store, name='store'),
	path('{request.user.Username}/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
]