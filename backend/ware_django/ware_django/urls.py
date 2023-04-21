from django.contrib import admin
from django.urls import path, include, re_path as url

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('djoser.urls')),
    path("api/", include('djoser.urls.authtoken')),
    url(r'^', include('stock_api.urls'))
]
