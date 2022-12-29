from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('demand', include('demand.urls')),
    path('geography', include('geography.urls')),
    path('skills', include('skills.urls')),
    path('last', include('last.urls')),
]
