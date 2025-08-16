from django.contrib import admin
from django.urls import path, include
# DENGEER CODE FOR PRODUCTION
from inventory.views import create_admin   # <- apne app ka naam lagao



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('inventory.urls')),
# DENGEER CODE FOR PRODUCTION
    path("create-admin/", create_admin),   # temporary route

]
