from django.urls import path, include

from mem.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),

    path('register/', Register.as_viev(), name='register'),
]