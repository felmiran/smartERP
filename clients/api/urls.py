from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from clients.api import views


urlpatterns = [
    # /clients
    url(r'^$', views.ClientListCreateView.as_view(), name='clients'),
    url(r'^(?P<pk>[0-9]+)/$', views.ClientDetailUpdateDeleteView.as_view(), name='clientdetail'),
    url(r'^(?P<pk>[0-9]+)/contacts/$', views.ClientContactListCreateView.as_view(), name='clientcontacts'),
    url(r'^contacts/(?P<pk>[0-9]+)/$', views.ClientContactDetailUpdateDeleteView.as_view(), name='clientcontactdetail'),
    # url(r'^create/$', views.ClientCreateView.as_view(), name='clientcreate')

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'xml'])