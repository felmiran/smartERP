from django.conf.urls import url
from . import views

app_name = 'sellers'

urlpatterns = [
    #sellers
    url(r'^$', views.SellerListView.as_view(), name="seller_list"),
    url(r'^add/$', views.CreateSeller.as_view(), name="seller-add"),
    url(r'^(?P<pk>[0-9]+)/update/$', views.UpdateSeller.as_view(), name='seller-update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.DeleteSeller.as_view(), name='seller-delete'),

]