from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, CartItem, Order, OrderItem
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm # Dagdag ito
from django.contrib import messages # Para sa alert messages

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'store/product_list.html', {'category': category, 'categories': categories, 'products': products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)
    return render(request, 'store/product_detail.html', {'product': product})

@login_required
def cart_detail(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.product.price * item.quantity for item in items)
    return render(request, 'store/cart_detail.html', {'items': items, 'total': total})

@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id, available=True)
    item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        item.quantity += 1
        item.save()
    return redirect('store:cart_detail')

@login_required
def cart_remove(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('store:cart_detail')

@login_required
def order_create(request):
    items = CartItem.objects.filter(user=request.user)
    if not items:
        return redirect('store:product_list')
    order = Order.objects.create(user=request.user)
    for item in items:
        OrderItem.objects.create(order=order, product=item.product, price=item.product.price, quantity=item.quantity)
    items.delete()
    return render(request, 'store/order_created.html', {'order': order})

# BAGONG REGISTER FUNCTION
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ayos! Gawa na ang account mo. Pwede ka na mag-login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})