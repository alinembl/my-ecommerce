
from django.conf.urls import url, patterns, include
from . import views

urlpatterns = [
   	url(r'^$', views.catalog, name='catalog'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^cart/remove/$', views.removefromcart, name='remove'),
    url(r'^cart/checkout/$', views.checkout,name='checkout'),
    url(r'^cart/checkout/complete/$', views.completeOrder,name='complete_order'),

]
