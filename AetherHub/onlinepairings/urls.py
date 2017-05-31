from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.event_list, name='event_list'),
    url(r'^event/(?P<pk>\d+)/$', views.event_details, name='event_details'),
    url(r'upload/', views.WER_upload, name='WER_upload') 
]