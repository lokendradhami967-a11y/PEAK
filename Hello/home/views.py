
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Product, CartItem
def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})


def login_view(request):
    return render(request, 'login.html')


def logout_view(request):
    if request.method == 'POST':
        auth_logout(request)
        return redirect('index')

    return render(request, 'logout.html')


def about(request):
    return render(request, 'about.html')

def footer(request):
    return render(request, 'footer.html')


@login_required
def add_to_cart(request,product_id):

    if request.method == "POST":
        product = get_object_or_404(product,id = product_id)

        cart_item,created = CartItem.objects.get_or_create(
            user = request.user,
            product = product,
            defaults = {'quantity':1}
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        messages.success(request, "Product added to cart!")

        return redirect('index')



