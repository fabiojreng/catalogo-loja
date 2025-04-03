from django.urls import path
from . import views


urlpatterns = [
    path("categories/", views.CategoryListView.as_view(), name="category_list"),
    path("categories/new/", views.CategoryCreateView.as_view(), name="category_create"),
    path(
        "categories/edit/<int:pk>/",
        views.CategoryUpdateView.as_view(),
        name="category_update",
    ),
    path(
        "categories/delete/<int:pk>/",
        views.CategoryDeleteView.as_view(),
        name="category_delete",
    ),
    path("products/", views.ProductListView.as_view(), name="admin-product_list"),
    path("products/new/", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "products/edit/<int:pk>/",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "products/delete/<int:pk>/",
        views.ProductDeleteView.as_view(),
        name="product_delete",
    ),
]
