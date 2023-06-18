from django.shortcuts import render
from .models import Item
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    items = Item.objects.all()
    return render(request, 'marketplace/home.html', {'items': items})
