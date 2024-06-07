from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path("", views.Addresses.as_view()),
    path("/<int:id>/", views.AddressesDetail.as_view(), name='address-detail'),
    path("/<int:user_id>/add", views.CreateUserAddress.as_view()),
    path('/<int:pk>/update', views.UpdateUserAddress.as_view()), 
    path('/<int:pk>/delete', views.DeleteUserAddress.as_view()),
    path("/getToken", obtain_auth_token)
]