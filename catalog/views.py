from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.db.models import Q
from django.shortcuts import get_object_or_404


class ProductListView(ListView):
    model = Product
    template_name = "products_list.html"
    context_object_name = "products"
    paginate_by = 6

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get("name")
        category_id = self.request.GET.get("category")

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(category__name__icontains=search)
            )

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.request.GET.get("category")

        if category_id:
            context["current_category"] = get_object_or_404(Category, id=category_id)
        else:
            context["current_category"] = None

        context["categories"] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_details.html"
    context_object_name = "product"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context
