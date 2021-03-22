from django import VERSION
from django.contrib import admin

if VERSION >= (2, 0):
    from django.urls import path
    urlpatterns = [
        path('admin/', admin.site.urls),
    ]
else:
    from django.conf.urls import url
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
    ]
