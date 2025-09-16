from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from .forms import CustomUsercreationForm
from django.views.decorators.cache import never_cache
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import Product
from django.contrib.auth.decorators import login_required
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



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
                auth_login(request, user)   # ✅ now no clash
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



def checkout(request):
    return render(request, 'checkout.html')

def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get("cart", {})

    if str(product.id) in cart:
        cart[str(product.id)]["quantity"] += 1
    else:
        cart[str(product.id)] = {
            "name": product.pName,
            "price": float(product.pPrice),
            "quantity": 1,
        }

    request.session["cart"] = cart
    request.session.modified = True

    total_qty = sum(item["quantity"] for item in cart.values())
    total_price = sum(item["price"] * item["quantity"] for item in cart.values())

    return JsonResponse({"cart_count": total_qty, "total_price": total_price})
def cart_view(request):
    cart = request.session.get("cart", {})
    return render(request, "cart.html", {"cart": cart})


# @login_required(login_url='login')
# def view_cart(request):
#     cart, created = Cart.objects.get_or_create(customUser=request.user)
#     cart_items = CartItem.objects.filter(cart=cart)
    
#     total_price = sum(item.subtotal for item in cart_items)
    
#     context = {'cart': cart, 'cart_items': cart_items, 'total_price': total_price}
#     return render(request, 'cart.html', context)

# # Corrected add_to_cart view
# @login_required(login_url='login')
# @csrf_exempt
# def add_to_cart(request, product_id):
#     product_instance = get_object_or_404(Product, id=product_id)
#     cart, _ = Cart.objects.get_or_create(customUser=request.user)

#     cart_item, created = CartItem.objects.get_or_create(
#         cart=cart, product=product_instance, defaults={'quantity': 1}
#     )
#     if not created:
#         cart_item.quantity += 1
#         cart_item.save()

#     # Optional: recalculate cart total
#     cart_items = CartItem.objects.filter(cart=cart)
#     total_price = sum(item.subtotal for item in cart_items)

#     return JsonResponse({
#     'product_id': cart_item.product.id,
#     'quantity': cart_item.quantity,
#     'subtotal': float(cart_item.subtotal),
#     'total_price': float(cart.total_price),
#     'total_items': cart.items.count(),
#     'pName': cart_item.product.pName
# })




# @login_required(login_url='login')
# @csrf_exempt
# def remove_from_cart(request, product_id):
#     cart_item = get_object_or_404(CartItem, cart__customUser=request.user, product__id=product_id)
#     cart_item.delete()
#     return JsonResponse({'product_id': product_id, 'removed': True})


# @login_required(login_url='login')
# @csrf_exempt
# def increment_quantity(request, product_id):
#     cart_item = get_object_or_404(CartItem, cart__customUser=request.user, product__id=product_id)
#     cart_item.quantity += 1
#     cart_item.save()
#     return JsonResponse({'product_id': product_id, 'quantity': cart_item.quantity, 'subtotal': float(cart_item.subtotal)})


# @login_required(login_url='login')
# @csrf_exempt
# def decrement_quantity(request, product_id):
#     cart_item = get_object_or_404(CartItem, cart__customUser=request.user, product__id=product_id)
#     if cart_item.quantity > 1:
#         cart_item.quantity -= 1
#         cart_item.save()
#         status = 'updated'
#     else:
#         cart_item.delete()
#         status = 'removed'
#     return JsonResponse({'product_id': product_id, 'status': status})



