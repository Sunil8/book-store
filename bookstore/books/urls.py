<<<<<<< HEAD
from django.conf.urls import url,include
from . import views
from django.conf import settings
urlpatterns = [
    url(r'^admin/$',views.dash_form,name='dash_form'),
    
]
# url(r'^pay/summary/(?P<value>\d+)/$', views.pay_summary, name='pay_summary')),
=======
from django.urls import path

urlpatterns = [

]
>>>>>>> 969f663db405fc631979e1e82c035e860ef9512e
