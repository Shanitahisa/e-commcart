from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from .forms import CustomUsercreationForm
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Product, Favorite
from django.contrib.auth.decorators import login_required
from cart.models import Cart, CartItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from cart.utils import get_user_cart



# Create your views here.

def signup(request):
    if request.method =="POST":
        form = CustomUsercreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = CustomUsercreationForm()
    return render(request, "signup.html", {"form":form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect ("index")    

@never_cache
def index(request):
    products = Product.objects.all()
    query = request.GET.get('q', '')  # get the search query
    if query:
        products = Product.objects.filter(pName__icontains=query)
    else:
        products = Product.objects.all()
    context = {
        'products': products, 
    }
    
    return render(request, 'index.html', context)

def product(request):
    return render(request, 'products.html')

@login_required
def clear_cart(request):
    cart = get_user_cart(request.user)
    cart.items.all().delete()
    return redirect("cart_detail")

@login_required
def checkout(request):
    cart = get_user_cart(request.user)
    return render(request, 'checkout.html', {'cart': cart})






@login_required
def add_to_favorites(request, pk):
    product = get_object_or_404(Product, pk=pk)
    fav, created = Favorite.objects.get_or_create(user=request.user, product=product)
    if created:
        messages.success(request, f"{product.pName} added to your favorites ")
    else:
        messages.info(request, f"{product.pName} is already in your favorites")
    return redirect(request.META.get('HTTP_REFERER', 'index'))


@login_required
def remove_from_favorites(request, pk):
    product = get_object_or_404(Product, pk=pk)
    Favorite.objects.filter(user=request.user, product=product).delete()
    messages.warning(request, f"{product.pName} removed from your favorites ")
    return redirect(request.META.get('HTTP_REFERER', 'favorites'))

@login_required
def my_favorites(request):
    favorites = Favorite.objects.filter(user=request.user).select_related("product")
    return render(request, "favorites.html", {"favorites": favorites})

