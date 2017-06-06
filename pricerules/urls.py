from django.conf.urls import url

from . import views

app_name = 'pricerules'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create/$' , views.create , name="create"),
    url(r'^(?P<price_rule_id>[0-9]+)/update_pr/$' , views.update , name="update"),
    url(r'^(?P<price_rule_id>[0-9]+)/delete_pr/$' , views.delete , name="delete"),
]
