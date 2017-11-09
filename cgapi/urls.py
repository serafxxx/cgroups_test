from django.conf.urls import url
from cgapi import views

urlpatterns = [

    # Please use digits and numbers to name cgroup. Trying to build url in a REST way
    url(r'^cgroups/(?P<cgname>[0-9,a-z,A-Z]+)$', views.CgroupAPIView.as_view()),
    url(r'^cgroups/(?P<cgname>[0-9,a-z,A-Z]+)/pids/(?P<pid>[0-9]+)$', views.PidAPIView.as_view()),
]