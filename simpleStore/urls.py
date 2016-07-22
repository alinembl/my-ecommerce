
from django.conf.urls import url,patterns, include
from django.contrib import admin
from store import urls as appurls
admin.autodiscover()

urlpatterns = [
    url(r'^$',include(appurls)),
    url(r'^admin/', admin.site.urls),

]
