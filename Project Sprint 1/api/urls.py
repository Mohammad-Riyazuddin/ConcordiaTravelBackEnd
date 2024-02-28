# travel/urls.py

from django.urls import path
from .views import PackageList, FlightDetail, FlightList, HotelList, HotelDetail, ActivityList, AcitivityDetail, BookingViewSet


urlpatterns = [
    path('flights/', FlightList.as_view(), name='flight-list-create'),
    path('hotels/', HotelList.as_view(), name='hotel-list-create'),
    path('activities/', ActivityList.as_view(), name='activity-list-create'),
    path('packages/', PackageList.as_view(), name='package-list'),
    path('bookings/', BookingViewSet.as_view(), name='Login'),
]
