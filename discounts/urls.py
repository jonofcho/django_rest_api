from django.conf.urls import url

from . import views


app_name = 'discounts'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<price_rule_id>[0-9]+)/$', views.detail, name='detail'),
]
