from django.urls import path
from . import views

urlpatterns = [
    path("", views.Addresses.as_view()),
     path("/<int:id>/", views.AddressesDetail.as_view(), name='address-detail'),
]