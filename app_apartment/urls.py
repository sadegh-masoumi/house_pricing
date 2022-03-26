from django.urls import path, include
from .views import ApartmentList, ApartmentListUser, \
    ApartmentCreate


urlpatterns = [
    path('apartments/', ApartmentList.as_view(), name='apartment_list'),
    path('apartments/create', ApartmentCreate.as_view(), name='apartment_create'),
    path('apartments/<email>', ApartmentListUser.as_view(), name='apartment_list_user'),
]
