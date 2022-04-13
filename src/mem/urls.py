from django.urls import path, include

from mem.views import RegisterView, AddMemView, HomeMemView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('add/', AddMemView, name='add_mem'),
    path('', HomeMemView.as_view(template_name='home.html'), name='home'),
]
