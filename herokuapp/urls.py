# dappx/urls.py
from django.conf.urls import url
from herokuapp import views
# SET THE NAMESPACE!
app_name = 'herokuapp'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^index/$',views.index,name='index'),
    url(r'^hello',views.hello,name="hello"),
    # url(r'^datas', views.datas, name='datas'),
]
