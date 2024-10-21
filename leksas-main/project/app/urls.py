from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView




urlpatterns=[
    path('register/student',StudentRegister.as_view(),name="studentregister"),
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh',TokenRefreshView.as_view()),
    path('UserProfile/',UserProfile.as_view()),
    path('UpdateProfile/',UpdateProfile.as_view()),
]