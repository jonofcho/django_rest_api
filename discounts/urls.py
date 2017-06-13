from django.conf.urls import url

from . import views


app_name = 'discounts'
urlpatterns = [
    url(r'^details/(?P<price_rule_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^create/(?P<price_rule_id>[0-9]+)/$' , views.create , name="create"),
]
