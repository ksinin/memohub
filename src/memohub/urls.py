from django.contrib import admin
from django.contrib.auth import views
from django.urls import path, include
from django.conf.urls.static import static
import memohub.settings as settings
from mem.views import HomeMemView, memadd

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeMemView.as_view(template_name='home.html'), name='home'),
    path('mem/', include('mem.urls')),
    path('addmem/', memadd, name='add_page'),
] + static(settings.STATIC_URL, document_root='/src/static')
