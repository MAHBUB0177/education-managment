from django.urls  import path

from .views import *

urlpatterns = [
    path('apiauth-branch-api/', BranchApiView.as_view(), name='apiauth-branch-api'),
    path('apiauth-country-api/', Country_Api_View.as_view(), name='apiauth-country-api'),
    path('apiauth-division-api/', Division_Api_View.as_view(), name='apiauth-division-api'),
    path('apiauth-upozila-api/', Upozila_Api_View.as_view(), name='apiauth-upozila-api'),

    path('apiauth-district-api/', District_Api_View.as_view(), name='apiauth-district-api'),

    path('apiauth-union-api/', Union_Api_View.as_view(), name='apiauth-union-api'),
]

