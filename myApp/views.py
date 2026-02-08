from django.shortcuts import render

from django.contrib.auth.decorators import login_required


from django.contrib.auth.decorators import user_passes_test

# Create your views here.
from django.http import HttpResponse


def home_view(request):
    # Django automatically looks in the 'templates' folder
    # so we just provide the path inside it.
    return render(request, "myApp/index.html")


from django.shortcuts import render, redirect
from .forms import ProductForm


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product
from .forms import ProductForm


# The "Add" View
@login_required
def add_product_view(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully!")
            return redirect("product_list_view")  # Redirect to our new list view
    else:
        form = ProductForm()
    return render(request, "myApp/add_product.html", {"form": form})


# The "Success/List" View
def product_list_view(request):
    # Fetch all products from the database
    all_products = Product.objects.all().order_by("-created_at")
    return render(request, "myApp/product_list.html", {"products": all_products})


# This is our custom authorization rule
def is_staff_member(user):
    return user.is_staff


@user_passes_test(is_staff_member)
def delete_product(request, pk):
    # This code only runs if the user is Authorized as staff
    product = Product.objects.get(id=pk)
    product.delete()
    return redirect("product_list_view")


# Function-based view
def product_list(request):
    product_list = Product.objects.all()
    return render(request, "product_list.html", {"products": product_list})


# class-based view
from django.views.generic import ListView


class ProductList(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "products"
