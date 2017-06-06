from django.conf.urls import url

from . import views


app_name = 'discounts'
urlpatterns = [
    url(r'^(?P<price_rule_id>[0-9]+)/details/$', views.detail, name='detail'),
    url(r'^(?P<price_rule_id>[0-9]+)/create/$' , views.create , name="create"),
]
