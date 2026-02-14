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


# my_app/views.py
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets, permissions
from .permissions import IsAuthorOrReadOnly

# from .permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated  # Make sure this is imported!


# 2. Writing a ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        # Check the version passed in the URL
        version = self.request.version

        if self.request.version == "v2":
            # Exclude posts made by the 'admin' user for a cleaner guest feed
            return Post.objects.exclude(author__username="Hanan")
        return Post.objects.all()

    filterset_fields = ["author", "title"]  # Users can now filter by these

    ordering_fields = ["created_at", "id"]  # Users can now sort by these

    # This line locks the view
    permission_classes = [IsAuthenticated]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]


# 1. Writing an APIView
class PostList(APIView):
    # read logic
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    # 2. Write logic
    def post(self, request):
        # We take the data the user sent (request.data) and give it to the serializer
        serializer = PostSerializer(data=request.data)

        # Check if the data is valid (e.g., is the email actually an email?)
        if serializer.is_valid():
            serializer.save()  # This calls the create() method in your serializer
            return Response(serializer.data, status=201)  # 201 means "Created"

        # If not valid, return the errors (e.g., "This field is required")
        return Response(serializer.errors, status=400)  # 400 means "Bad Request"
