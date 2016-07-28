
from django.conf.urls import url, include
import django.contrib.auth.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'', include('store.urls')),
    url(r'^admin/', admin.site.urls),

]


