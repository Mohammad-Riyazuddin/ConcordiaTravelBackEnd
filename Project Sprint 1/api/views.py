# travel/views.py

from rest_framework import generics
from rest_framework import viewsets
from .models import Package, Flight, Hotel, Activity, Booking
from .serializers import PackageSerializer, FlightSerializer, HotelSerializer, ActivitySerializer, BookingSerializer

class PackageList(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['flight_serializer'] = FlightSerializer
        context['hotel_serializer'] = HotelSerializer
        context['activity_serializer'] = ActivitySerializer
        return context

class PackageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    
class FlightList(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class FlightDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class HotelList(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class HotelDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer

class ActivityList(generics.ListCreateAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    
class AcitivityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    
class BookingViewSet(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def perform_create(self, serializer):
        # Automatically set the logged-in user as the booking user
        serializer.save(user=self.request.user)