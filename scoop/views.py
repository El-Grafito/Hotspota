from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product
from .models import Category
from .forms import ProductForm


def home(request):
        categorys = Category.objects.all()
        context = {
        'categorys': categorys,
        }
        return render(request,'scoop/main.html', context)

def cat(request):
    return render(
        request,
        'scoop/cat.html'
    )

def info(request):
    return render(
        request,
        'scoop/info.html'
    )

def all(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'scoop/all.html', context)

def product_page(request, pk, category_slug):
    product = Product.objects.get(id=pk)
    category = Category.objects.get(slug=category_slug)
    context = {
        'product': product,
        'category_slug': category,
    }
    return render(request, 'scoop/product_page.html', context)

def categorya(request, slug): 
     categorya = Category.objects.get(slug=slug)
     products = categorya.product_set.all()
     productss = Product.objects.all()
     context = {
          'categorya': categorya,
          'products': products,
          'productss': productss

     }
     return render(request, 'scoop/categorya.html', context)

def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            Product.objects.create(
                title=cd['title'],
                description=cd['description'],
                price=cd['price'],
                image=cd['image'],
                category=cd['category'],
            )
            return redirect(to='all')
    else:
        form = ProductForm()

    context = {
        'form': form,

    }
    return render(request, 'scoop/create.html', context)

