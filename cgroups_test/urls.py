from django.conf.urls import url, include


urlpatterns = [
    url(r'^cgapi/', include('cgapi.urls')),
]
