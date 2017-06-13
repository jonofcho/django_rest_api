from django.conf.urls import url

from . import views

app_name = 'pricerules'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$' , views.create , name="create"),
    url(r'^update/(?P<price_rule_id>[0-9]+)/$' , views.update , name="update"),
    url(r'^delete/(?P<price_rule_id>[0-9]+)/$' , views.delete , name="delete"),
]
