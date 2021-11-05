from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('webadm/', admin.site.urls),
    path('',include('appauth.urls')),
	path('',include('hrm.urls')),
    path('',include('edu.urls')),
    path('',include('apiauth.urls')),
	path('',include('apihrm.urls')),
    path('',include('apiedu.urls')),
]