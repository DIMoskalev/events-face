from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('src.events.urls')),
    path('users/', include('src.users.urls', namespace='users')),
]
