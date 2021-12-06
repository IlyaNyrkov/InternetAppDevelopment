from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('about', views.index, name='about'),
    path('addCrypto', views.add_crypto_info, name='addCrypto'),
    path('exploreCrypto', views.explore_crypto, name='exploreCrypto')
]

urlpatterns += staticfiles_urlpatterns()