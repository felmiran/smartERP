from django.conf.urls import url
from . import views

app_name = 'clients'

urlpatterns = [
    url(r'^$', views.ClientListView.as_view(), name='client_list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ClientDetailView.as_view(), name='client_detail'),
    url(r'^(?P<pk>[0-9]+)/contacts/$', views.ClientContactListView.as_view(), name='contact_list'),
    url(r'^client_contacts/(?P<pk>[0-9]+)/$', views.ClientContactDetailView.as_view(), name='contact_detail'),
    url(r'^add/$', views.CreateClient.as_view(), name='client-add'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateClient.as_view(), name='client-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.UpdateClient.as_view(), name='client-delete'),




]