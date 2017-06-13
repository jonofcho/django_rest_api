from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^discounts/', include('discounts.urls')),
    url(r'^pricerules/', include('pricerules.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^pr_api/', include('api_requests.urls')),
]
