from django.conf.urls import url
from .views import reg,home,login
app_name='regandloginapp'
urlpatterns=[
    url(r'^$',home,name='home'),
    url(r'^reg$',reg,name='reg'),
    url(r'^login$',login,name='login'),
]