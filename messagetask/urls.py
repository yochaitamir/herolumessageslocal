from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from messagetask import views

urlpatterns = [
url(r'^$', views.index,name="index"),
url(r'^write_message/$', views.write_message,name="write_message"),
url(r'^get_all_messages/$',views.get_all_messages,name='get_all_messages'),
url(r'^get_all_unread_messages/(?P<user>\w+)/$',views.get_all_unread_messages,name='get_all_unread_messages'),
url(r'^delete_message/(?P<mpk>\d+)/(?P<user>\w+)/$',views.delete_message,name='delete_message'),
url(r'^login/$',views.login,name='login'),    
]
