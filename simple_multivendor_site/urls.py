from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
import re


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls")),
    path("vendor/", include("vendor.urls")),
    path("product/", include("product.urls")),
    path("cart/", include("cart.urls")),
    path("order/", include("order.urls")),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
