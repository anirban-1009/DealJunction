from django.shortcuts import render, redirect
from users.views import login_and_email_verified_required
from users.models import User
from .models import Product
from cart.cart import Cart
from django.http import HttpResponse


def home(request):
    items = Product.objects.all()
    return render(request, 'marketplace/home.html', {'items': items})


@login_and_email_verified_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_and_email_verified_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_and_email_verified_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_and_email_verified_required
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_and_email_verified_required
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("home")


@login_and_email_verified_required
def cart_detail(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    cart = Cart(request)
    data = cart.session.items()
    total = 0
    for key, value in data:
       if type(value) == dict:
        for item in value.values():
            price = float(item['price'])*float(item['quantity'])
            total += price
    return render(request, 'marketplace/cart_detail.html', {'total': total})

@login_and_email_verified_required
def checkout(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    cart = Cart(request)
    data = cart.session.items()
    total = 0
    for key, value in data:
       if type(value) == dict:
        for item in value.values():
            price = float(item['price'])*float(item['quantity'])
            total += price
    user.wallet -= total
    user.save()
    return redirect('cart_clear')