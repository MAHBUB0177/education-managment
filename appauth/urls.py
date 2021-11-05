from django.urls import path

##### For Image Upload
from django.conf import settings
from django.conf.urls.static import static

from .views import *

urlpatterns = [
     path('appauth/', HomeView.as_view(), name='appauth'),
     path('', HomeView.as_view(), name=''),
     path('appauth-home/', appauth_home, name='appauth-home'),
     path('appauth-login', login_view, name='appauth-login'),  
     path('appauth-logout/', logout_view, name='appauth-logout'),
     path('appauth-reset-password/', reset_password.as_view(), name='appauth-reset-password'),
     path('appauth-reset-passwordpost', reset_user_password, name='appauth-reset-passwordpost'),
     path("appauth-dashboard", DashboardView, name='appauth-dashboard'),
     path('appauth-app-user', CreateUser.as_view() , name ='appauth-app-user'),
     path('appauth-application-users', ApplicationUserList.as_view(), name='appauth-application-users'),
     path('appauth-branch-createlist', appauth_branch_view.as_view(), name='appauth-branch-createlist'),
     path('appauth-branch-insert', appauth_branch_insert, name='appauth-branch-insert'),
     path('appauth-branch-edit/<slug:id>', appauth_branch_edit, name='appauth-branch-edit'),
     
     path('appauth-country-createlist', appauth_country_view.as_view(), name='appauth-country-createlist'),
     path('appauth-country-insert', appauth_country_insert, name='appauth-country-insert'),
     path('appauth-country-edit/<slug:id>', appauth_country_edit, name='appauth-country-edit'),

     
    

     path('appauth-division-createlist', appauth_division_view.as_view(), name='appauth-division-createlist'),
     path('appauth_division_insert', appauth_division_insert, name='appauth_division_insert'),
     path('appauth_division_edit/<slug:id>', appauth_division_edit, name='appauth_division_edit'),


    path('appauth-upozila-createlist', appauth_upozila_view.as_view(), name='appauth-upozila-createlist'),
    path('appauth_upozila_insert', appauth_upozila_insert, name='appauth_upozila_insert'), 
    path('appauth_upozila_edit/<slug:id>', appauth_upozila_edit, name='appauth_upozila_edit'),


    path('appauth-district-createlist', appauth_district_view.as_view(), name='appauth-district-createlist'),
     path('appauth_district_insert', appauth_district_insert, name='appauth_district_insert'),
     path('appauth_district_edit/<slug:id>', appauth_district_edit, name='appauth_district_edit'),


    path('appauth-union-createlist', appauth_union_view.as_view(), name='appauth-union-createlist'),
     path('appauth_union_insert', appauth_union_insert, name='appauth_union_insert'),
     path('appauth_union_edit/<slug:id>', appauth_union_edit, name='appauth_union_edit'),
     

]

#### For Image Upload
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#managecollect