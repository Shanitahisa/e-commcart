from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns=[
    path("",views.index, name="index"),
    path("index/",views.index,name="index"),
    path("product/",views.product, name="product"),
    # path("cart/", views.cart, name="cart"),
    path("signup/", views.signup, name="signup"),
    path("checkout/", views.checkout, name="checkout"),
    path("login/",views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    # path("ajax/add-to-cart/", views.ajax_add_to_cart, name="ajax_add_to_cart"),

    # path('cart/', views.view_cart, name='view_cart'),
    # path('add_to_cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('remove_from_cart/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    # path('increment_quantity/<int:product_id>/', views.increment_quantity, name='increment_quantity'),
    # path('decrement_quantity/<int:product_id>/', views.decrement_quantity, name='decrement_quantity'),
    path("add-to-cart/<int:productId>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart_view, name="cart"),

]


    