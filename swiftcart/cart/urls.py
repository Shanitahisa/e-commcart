from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[

path("cart/", views.cart_detail, name="cart_detail"),
path("cart/add/<int:product_id>/", views.add_to_cart, name="add_to_cart"),
path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
path("cart/update/<int:item_id>/", views.update_cart, name="update_cart"),
]