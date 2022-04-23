from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import memohub.settings as settings
from mem.views import HomeMemView, RegisterView, FollowingMemView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mem/', include('mem.urls')),
    path('', HomeMemView.as_view(template_name='home.html'), name='home'),
    path('following_feed/', FollowingMemView.as_view(), name='following_mem'),
    path('', include('django.contrib.auth.urls')),
    path('register/', RegisterView.as_view(), name='register'),
] + static(settings.STATIC_URL, document_root='/src/static')
