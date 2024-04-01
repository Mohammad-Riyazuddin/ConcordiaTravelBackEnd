# travel/urls.py

from django.urls import path
from .views import PackageList, PackageDetail, FlightDetail, FlightList, HotelList, HotelDetail, ActivityList, \
    AcitivityDetail, BookingViewSet, BookingDetail, RegisterView, LoginView, LogoutView, UserDetailsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('flights/', FlightList.as_view(), name='flight-list-create'),
    path('hotels/', HotelList.as_view(), name='hotel-list-create'),
    path('activities/', ActivityList.as_view(), name='activity-list-create'),
    path('packages/', PackageList.as_view(), name='package-list'),
    path('bookings/', BookingViewSet.as_view(), name='Bookings'),
    path('bookings/<int:pk>/', BookingDetail.as_view(), name='Bookings-Details'),
    path('packages/<int:pk>/', PackageDetail.as_view(), name='package-detail'),
    path('flights/<int:pk>/', FlightDetail.as_view(), name='flight-detail'),
    path('activities/<int:pk>/', AcitivityDetail.as_view(), name='activity-detail'),
    path('hotels/<int:pk>/', HotelDetail.as_view(), name='hotel-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('user-details/', UserDetailsView.as_view(), name='user-details'),
]
