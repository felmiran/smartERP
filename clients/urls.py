from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from clients import views

urlpatterns = [
    # /clients
    url(r'^$', views.ClientView.as_view(), name='clients'),
    url(r'^(?P<pk>[0-9]+)/$', views.ClientDetailView.as_view(), name='clientdetail'),
    url(r'^(?P<pk>[0-9]+)/contacts/$', views.ClientContactView.as_view(), name='clientcontacts'),
    url(r'^contacts/(?P<pk>[0-9]+)/$', views.ClientContactDetailView.as_view(), name='clientcontactdetail'),

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html', 'xml'])