from django.conf.urls import url

from . import views


app_name = 'discounts'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<price_rule_id>[0-9]+)/details/$', views.detail, name='detail'),
    url(r'^new_pr/$' , views.new_pr , name="new_pr"),
    url(r'^(?P<price_rule_id>[0-9]+)/update_pr/$' , views.update_pr , name="update_pr"),
    url(r'^(?P<price_rule_id>[0-9]+)/delete_pr/$' , views.delete_pr , name="delete_pr"),
    url(r'^(?P<price_rule_id>[0-9]+)/new_dc/$' , views.new_dc , name="new_dc"),
    url(r'^(?P<discount_id>[0-9]+)/dc_details/$', views.dc_details, name='dc_detail'),

]
