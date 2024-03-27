# travel/serializers.py

from rest_framework import serializers
from .models import Package, Flight, Hotel, Activity, Booking
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token


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


class PackageSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)
    hotel = HotelSerializer(read_only=True)
    activity = ActivitySerializer(read_only=True)

    class Meta:
        model = Package
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    package_details = PackageSerializer(source='package', read_only=True)
    class Meta:
        model = Booking
        fields = '__all__'
    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Only include cancel_date in the response if it's not None
        if instance.cancel_date is None:
            del data['cancel_date']
        return data


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'user_type')
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


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'user_type')
        extra_kwargs = {'user_type': {'read_only': False}}