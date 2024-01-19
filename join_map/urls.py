from django.contrib import admin
from django.urls import path
from target.views import target_map

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', target_map, name='target_map'),
]
