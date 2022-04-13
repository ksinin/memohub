from django.urls import path, include
from django.contrib.auth import views
from mem.views import RegisterView, memadd

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('addmem/', memadd, name='add_page'),
]
