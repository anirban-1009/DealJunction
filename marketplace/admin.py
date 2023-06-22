from django.contrib import admin
from .models import Item, Product
# class CartItemInline(admin.TabularInline):
#     model = CartItem
#     extra = 0



class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

# class CartAdmin(admin.ModelAdmin):
#     inlines = [CartItemInline]


admin.site.register(Item, ItemAdmin)
admin.site.register(Product, ProductAdmin)
