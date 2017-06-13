from django.conf.urls import url, include

from rest_framework import routers

from . import views

app_name = 'api_requests'
urlpatterns = [
    url(r'^api/(?P<price_rule_id>[0-9]+)/', views.get_pr , name="pr_viewset"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
