# travel/serializers.py

from rest_framework import serializers
from .models import Package, Flight, Hotel, Activity, Booking
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import viewsets


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = '__all__'


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class PackageDetailSerializer(serializers.ModelSerializer):
    flight = FlightSerializer()
    hotel = HotelSerializer()
    activity = ActivitySerializer()

    class Meta:
        model = Package
        fields = '__all__'


class PackageCreateSerializer(serializers.ModelSerializer):
    flight = serializers.PrimaryKeyRelatedField(queryset=Flight.objects.all())
    hotel = serializers.PrimaryKeyRelatedField(queryset=Hotel.objects.all())
    activity = serializers.PrimaryKeyRelatedField(queryset=Activity.objects.all())

    class Meta:
        model = Package
        fields = '__all__'


User = get_user_model()


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)


class BookingSerializer(serializers.ModelSerializer):
    package_details = PackageDetailSerializer(source='package', read_only=True)
    user_id = UserDetailsSerializer()

    class Meta:
        model = Booking
        fields = '__all__'


class BookingCreateSerializer(serializers.ModelSerializer):
    package_details = PackageDetailSerializer(source='package', read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Booking
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Only include cancel_date in the response if it's not None
        if instance.cancel_date is None:
            del data['cancel_date']
        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'is_staff')  # Remove 'user_type'
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = User.objects.filter(username=data['username']).first()
        if user and user.check_password(data['password']):
            return user
        raise serializers.ValidationError("Incorrect Credentials")


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ('key',)


class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return PackageCreateSerializer
        else:
            return PackageDetailSerializer


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return BookingCreateSerializer
        else:
            return BookingSerializer

