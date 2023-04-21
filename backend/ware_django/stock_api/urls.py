from django.urls import re_path as url
from stock_api import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^stock$',views.stockApi),
    url(r'^stock/([0-9]+)$',views.stockApi),

    url(r'^order$',views.orderApi),
    url(r'^order/([0-9]+)$',views.orderApi),

    url(r'^sector$',views.sectorApi),
    url(r'^sector/([0-9]+)$',views.sectorApi),

    url(r'^shelf$',views.shelfApi),
    url(r'^shelf/([0-9]+)$',views.shelfApi),
    
    url(r'^map$',views.mapApi),
    url(r'^map/([0-9]+)$',views.mapApi),

    url(r'^stock/savefile',views.SaveFile),
    url(r'^map/savefile',views.SaveFile)
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
