from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import memohub.settings as settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mem/', include('mem.urls')),
] + static(settings.STATIC_URL, document_root='/src/static')
