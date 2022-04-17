from django.urls import path, include

from mem.views import RegisterView, AddMemView, YourMemView, DeleteMemView, EditMemView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
    path('add_mem/', AddMemView.as_view(), name='addmem'),
    path('your_memes/', YourMemView.as_view(), name='yourmemes'),
    path('delete_mem/<int:mem_id>/', DeleteMemView.as_view(), name='deletemem'),
    path('edit_mem/<int:mem_id>/', EditMemView.as_view(), name='editmem'),
]
