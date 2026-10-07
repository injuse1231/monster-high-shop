from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .cart import Cart
from django.contrib import messages

def index(request):
    products = Product.objects.all()
    cart = Cart(request)
    return render(request, 'home/catalog.html', {'products': products, 'cart': cart})

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    messages.success(request, f'«{product.name}» добавлена в корзину!')
    return redirect(request.META.get('HTTP_REFERER', '/'))

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'home/cart.html', {'cart': cart})

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')

