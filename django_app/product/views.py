from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

def home(request):
    products = Product.objects.all()
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'home.html', {'products': products, 'form': form})

