from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect


def home_redirect(request):
    return redirect("product_list")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_redirect, name="home"),
    path("produtos/", include("catalog.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
