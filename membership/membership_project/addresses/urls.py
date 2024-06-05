from django.urls import path
from . import views

urlpatterns = [
    path("", views.Addresses.as_view()),
    path("/<int:id>/", views.AddressesDetail.as_view(), name='address-detail'),
    path("/<int:user_id>/add", views.CreateUserAddress.as_view()),
    path('/<int:pk>/update', views.UpdateUserAddress.as_view()), 
]