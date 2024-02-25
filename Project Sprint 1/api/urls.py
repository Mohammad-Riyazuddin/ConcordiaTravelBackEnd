# travel/urls.py

from django.urls import path
from .views import PackageList, PackageDetail, FlightDetail, FlightList, HotelList, HotelDetail, ActivityList, AcitivityDetail

urlpatterns = [
    path('packages/', PackageList.as_view(), name='package-list'),
    path('packages/<int:pk>/', PackageDetail.as_view(), name='package-detail'),
    path('packages/flights/', FlightList.as_view(), name='flight-listl'),
    path('packages/<int:pk>/flights/', FlightDetail.as_view(), name='flight-detail'),
    
    path('packages/hotels/', HotelList.as_view(), name='hotel-listl'),
    path('packages/<int:pk>/hotels/', HotelDetail.as_view(), name='hotel-detail'),
    
    path('packages/activities/', ActivityList.as_view(), name='activity-listl'),
    path('packages/<int:pk>/activities/', AcitivityDetail.as_view(), name='activity-detail'),
]
