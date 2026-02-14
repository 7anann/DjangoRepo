# myapp/urls.py
from django.urls import path, include
from . import views
from .views import PostList, PostViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r"", PostViewSet)  # This creates /posts/ and /posts/id/ automatically

urlpatterns = [
    # When the path is empty '', it triggers home_view
    path("home", views.home_view, name="home"),
    # When the path is 'add-product', it triggers add_product_view
    path("add-product/", views.add_product_view, name="add_product"),
    # This is the "success_url"
    path("list/", views.product_list_view, name="product_list_view"),
    # Add url to delete product
    path("delete/<int:pk>/", views.delete_product, name="delete"),
    path("posts_API/", PostList.as_view()),  # You must use .as_view()
    path("", include(router.urls)),
]
