from django.conf.urls import include, url
from . import views

urlpatterns = [
    #signin
    url('signin',views.signin,name='signin'),

    #signup
    url('signup',views.signup,name='signup'),

    #signout
    url('signout',views.signout,name='signout'),

    #jsonfolder
    url(r'^$', views.index,name='index'),

    #1
    url(r'^(?P<admin_id>[0-9]+)/$',views.particulars,name='particulars'),

    #data
    url('data' ,views.parseData, name="data")
]
