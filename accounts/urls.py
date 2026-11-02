from django.urls import path
from accounts.views import AdminRegisterView,UserregisterView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns=[

    path("admin/",AdminRegisterView.as_view()),

    path("user/",UserregisterView.as_view()),
    
    path("user/token/",TokenObtainPairView.as_view()),
    
    path("user/token/refresh/",TokenRefreshView.as_view()),
]