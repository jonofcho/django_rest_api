from django.conf.urls import url

from . import views


app_name = 'discounts'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<price_rule_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^new_pr/$' , views.new_pr , name="new_pr"),
    url(r'^new_dc/$' , views.new_dc , name="new_dc")

]
