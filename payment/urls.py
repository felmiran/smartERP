from django.conf.urls import url
from . import views

app_name = "payment"

urlpatterns = [
    # payment
    url(r'^payform/$', views.PayformListView.as_view(), name='payform_list'),
    url(r'^payform/add/$', views.CreatePayform.as_view(), name='payform-add'),
    url(r'^payform/(?P<pk>[0-9]+)/update/$', views.UpdatePayform.as_view(), name='payform-update'),
    url(r'^payform/(?P<pk>[0-9]+)/delete/$', views.DeletePayform.as_view(), name='payform-delete'),

    # payment
    url(r'^credit_cond/$', views.CreditConditionListView.as_view(), name='creditcondition_list'),
    url(r'^credit_cond/add/$', views.CreateCreditCondition.as_view(), name='creditcondition-add'),
    url(r'^credit_cond/(?P<pk>[0-9]+)/update/$', views.UpdateCreditCondition.as_view(), name='creditcondition-update'),
    url(r'^credit_cond/(?P<pk>[0-9]+)/delete/$', views.DeleteCreditCondition.as_view(), name='creditcondition-delete'),
]