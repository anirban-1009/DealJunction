from django.shortcuts import render, redirect
from .models import Item
from django.contrib.auth.decorators import login_required
from users.models import User
from .models import Cart

@login_required
def home(request):
    items = Item.objects.all()
    return render(request, 'marketplace/home.html', {'items': items})

@login_required
def buy_item(request, id):
    current_user = request.user.id
    try:
        cart=Cart.objects.filter(id=current_user)
        print(cart.all)
    except User.DoesNotExist:
        print("User Not found")
    
    return redirect('home')