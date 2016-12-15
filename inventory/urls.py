from django.conf.urls import url
from . import views

app_name = 'inventory'


urlpatterns = [
    # attributes
    url(r'^attributes/$', views.AttributeListView.as_view(), name='attribute_list'),
    url(r'^attributes/add/$', views.CreateAttribute.as_view(), name='attribute-add'),
    url(r'^attributes/(?P<pk>[0-9]+)/update/$', views.UpdateAttribute.as_view(), name='attribute-update'),
    url(r'^attributes/(?P<pk>[0-9]+)/delete/$', views.DeleteAttribute.as_view(), name='attribute-delete'),


]

