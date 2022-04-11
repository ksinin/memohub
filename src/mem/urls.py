from django.urls import path, include
from django.contrib.auth import views
from mem.views import Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register')
]