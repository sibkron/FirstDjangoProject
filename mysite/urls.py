from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webexample/', include('webexample.urls')),
    path('', include('mainApp.urls')),
]
