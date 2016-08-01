
from django.conf.urls import url, patterns, include
from . import views

urlpatterns = [
   	url(r'^$', views.catalog, name='catalog'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^cart/remove/$', views.removefromcart, name='remove'),


]
