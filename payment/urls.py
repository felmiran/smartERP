from django.conf.urls import url
from . import views

app_name = "payment"

urlpatterns = [
    # payment
    url(r'^payform/$', views.PayformListView.as_view(), name='payform_list'),
    url(r'^payform/add/$', views.CreatePayform.as_view(), name='payform-add'),
    url(r'^payform/(?P<pk>[0-9]+)/update/$', views.UpdatePayform.as_view(), name='payform-update'),
    url(r'^payform/(?P<pk>[0-9]+)/delete/$', views.DeletePayform.as_view(), name='payform-delete'),

    # credit condition
    url(r'^credit_cond/$', views.CreditConditionListView.as_view(), name='creditcondition_list'),
    url(r'^credit_cond/add/$', views.CreateCreditCondition.as_view(), name='creditcondition-add'),
    url(r'^credit_cond/(?P<pk>[0-9]+)/update/$', views.UpdateCreditCondition.as_view(), name='creditcondition-update'),
    url(r'^credit_cond/(?P<pk>[0-9]+)/delete/$', views.DeleteCreditCondition.as_view(), name='creditcondition-delete'),

    # inventory movement type
    url(r'^invmov_type/$', views.InventoryMovementTypeListView.as_view(), name='inventorymovementtype_list'),
    url(r'^invmov_type/add/$', views.CreateInventoryMovementType.as_view(), name='inventorymovementtype-add'),
    url(r'^invmov_type/(?P<pk>[0-9]+)/update/$', views.UpdateInventoryMovementType.as_view(), name='inventorymovementtype-update'),
    url(r'^invmov_type/(?P<pk>[0-9]+)/delete/$', views.DeleteInventoryMovementType.as_view(), name='inventorymovementtype-delete'),

    # sale doc type
    url(r'^saledoctype/$', views.SaleDocTypeListView.as_view(), name='saledoctype_list'),
    url(r'^saledoctype/add/$', views.CreateSaleDocType.as_view(), name='saledoctype-add'),
    url(r'^saledoctype/(?P<pk>[0-9]+)/update/$', views.UpdateSaleDocType.as_view(), name='saledoctype-update'),
    url(r'^saledoctype/(?P<pk>[0-9]+)/delete/$', views.DeleteSaleDocType.as_view(), name='saledoctype-delete'),

    # purchase doc type
    # url(r'^purchasedoctype/$', views.PurchaseDocTypeListView.as_view(), name='purchasedoctype_list'),
    # url(r'^purchasedoctype/add/$', views.CreatePurchaseDocType.as_view(), name='purchasedoctype-add'),
    # url(r'^purchasedoctype/(?P<pk>[0-9]+)/update/$', views.UpdatePurchaseDocType.as_view(), name='purchasedoctype-update'),
    # url(r'^purchasedoctype/(?P<pk>[0-9]+)/delete/$', views.DeletePurchaseDocType.as_view(), name='purchasedoctype-delete'),

    # tax
    # url(r'^tax/$', views.TaxListView.as_view(), name='tax_list'),
    # url(r'^tax/add/$', views.CreateTax.as_view(), name='tax-add'),
    # url(r'^tax/(?P<pk>[0-9]+)/update/$', views.UpdateTax.as_view(), name='tax-update'),
    # url(r'^tax/(?P<pk>[0-9]+)/delete/$', views.DeleteTax.as_view(), name='tax-delete'),

]