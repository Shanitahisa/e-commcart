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
    path("signup/", views.signup, name="signup"),
    path("clear/", views.clear_cart, name="clear_cart"),
    path("checkout/", views.checkout, name="checkout"),

    path("login/",views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
  
    path("favorites/", views.my_favorites, name="my_favorites"), 
    path("favorites/add/<int:pk>/", views.add_to_favorites, name="add_to_favorites"),
    path("favorites/remove/<int:pk>/", views.remove_from_favorites, name="remove_from_favorites"),

]


    