from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^discounts/', include('discounts.urls')),
    url(r'^admin/', admin.site.urls),
]
