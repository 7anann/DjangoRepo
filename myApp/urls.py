# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # When the path is empty '', it triggers home_view
    path("", views.home_view, name="home"),
    # When the path is 'add-product', it triggers add_product_view
    path("add-product/", views.add_product_view, name="add_product"),
    # This is the "success_url"
    path("list/", views.product_list_view, name="product_list_view"),
    # Add url to delete product
    path("delete/<int:pk>/", views.delete_product, name="delete"),
]
