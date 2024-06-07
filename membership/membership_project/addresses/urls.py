from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path("", views.Addresses.as_view()),
    path("<int:id>/", views.AddressesDetail.as_view(), name='address-detail'),
    path("<int:user_id>/add", views.CreateUserAddress.as_view()),
    path('<int:pk>/update', views.UpdateUserAddress.as_view()), 
    path('<int:pk>/delete', views.DeleteUserAddress.as_view()),
    path("getToken", obtain_auth_token),
    path('login/simpleJWT', TokenObtainPairView.as_view()),
    path('login/simpleJWT/refresh', TokenRefreshView.as_view()),
    path('login/simpleJWT/verify', TokenVerifyView.as_view()),
]