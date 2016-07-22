
from django.conf.urls import url, patterns, include
from . import views

urlpatterns = [
   	url(r'^$',views.catalog,name="catalog"),


]
