from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('about', views.index, name='about')
]

urlpatterns += staticfiles_urlpatterns()