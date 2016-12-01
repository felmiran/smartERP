from django.conf.urls import url
from . import views

app_name = "management"

urlpatterns = [
    #warehouse
    url(r'^warehouse/$', views.WarehouseListView.as_view(), name='warehouse_list'),
    url(r'^warehouse/add/$', views.CreateWarehouse.as_view(), name='warehouse-add'),
    url(r'^warehouse/(?P<pk>[0-9]+)/update/$', views.UpdateWarehouse.as_view(), name='warehouse-update'),
    url(r'^warehouse/(?P<pk>[0-9]+)/delete/$', views.DeleteWarehouse.as_view(), name='warehouse-delete'),

    #branch



]
