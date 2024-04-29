# travel/views.py

from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token

from .models import Package, Flight, Hotel, Activity, Booking
from .serializers import PackageDetailSerializer, FlightSerializer, HotelSerializer, ActivitySerializer, BookingSerializer, \
    UserSerializer, LoginSerializer, UserDetailsSerializer, PackageCreateSerializer, BookingCreateSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import Group, User


class PackageList(generics.ListCreateAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageCreateSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['flight_serializer'] = FlightSerializer
        context['hotel_serializer'] = HotelSerializer
        context['activity_serializer'] = ActivitySerializer
        return context


class PackageDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageDetailSerializer


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
    serializer_class = BookingCreateSerializer


class BookingDetail(generics.RetrieveUpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        print(request.data.get('user_type'))
        if serializer.is_valid():
            user = serializer.save()
            # Determine user type based on username
            if request.data.get('user_type') == 'admin':
                group, _ = Group.objects.get_or_create(name='Admin')
                user.is_staff = True
            elif request.data.get('user_type') == 'agent':
                group, _ = Group.objects.get_or_create(name='Agent')
                user.is_staff = True
            elif request.data.get('user_type') == 'customer':
                group, _ = Group.objects.get_or_create(name='Customer')
                user.is_staff = False
            user.groups.add(group)
            # Generate token for the user
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_id': user.id, 'user_type': user.is_staff}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'userId': user.id, 'isStaff': user.is_staff}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


class UserDetailsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserDetailsSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserDetailsSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
