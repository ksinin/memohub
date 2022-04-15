from django.urls import path, include

from mem.views import RegisterView, AddMemView, YourMemView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('add_mem/', AddMemView.as_view(), name='addmem'),
    path('your_memes/', YourMemView.as_view(), name='yourmemes')


]
