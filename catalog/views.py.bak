from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Contact
from .forms import ProductForm


def home(request):
    # Дополнительное задание: вывод последних 5 продуктов в консоль
    latest_products = Product.objects.all().order_by('-created_at')[:5]
    print("Последние 5 продуктов:")
    for product in latest_products:
        print(f"- {product.name} ({product.price})")

    context = {
        'latest_products': latest_products
    }
    return render(request, 'catalog/home.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'catalog/product_detail.html', context)


def contacts(request):
    contact_info = Contact.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f"Новое сообщение от {name} ({phone}): {message}")

    context = {
        'contact_info': contact_info
    }
    return render(request, 'catalog/contacts.html', context)


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'catalog/product_form.html', context)