from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('people/', include('people.urls')),
    path('books/', include('books.urls')),
    path('artifacts/', include('artifacts.urls')),
    path('vehicles/', include('vehicles.urls')),
    path('api/', include('api.urls'))
]
