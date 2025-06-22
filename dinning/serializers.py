from rest_framework import serializers
from django.contrib.auth.models import User
from .models import DiningPlace, Reservation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class DiningPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiningPlace
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
        read_only_fields = ['user']
