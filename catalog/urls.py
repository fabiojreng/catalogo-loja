from django.urls import path
from . import views

urlpatterns = [
    path("product/list/", views.ProductListView.as_view(), name="product_list"),
    path(
        "product/<int:pk>/details/",
        views.ProductDetailView.as_view(),
        name="product_details",
    ),
]
