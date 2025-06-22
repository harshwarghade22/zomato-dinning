from rest_framework import generics, permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import DiningPlace, Reservation
from .serializers import UserSerializer, DiningPlaceSerializer, ReservationSerializer
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Sum


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddDiningPlaceView(generics.CreateAPIView):
    queryset = DiningPlace.objects.all()
    serializer_class = DiningPlaceSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
def search_dining_places(request):
    query = request.GET.get('q', '')
    results = DiningPlace.objects.filter(name__icontains=query)
    serializer = DiningPlaceSerializer(results, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def check_availability(request, pk):
    dining_place = DiningPlace.objects.get(id=pk)
    reservations = Reservation.objects.filter(dining_place=dining_place)
    total_booked = reservations.aggregate(
        total=Sum('number_of_people'))['total'] or 0
    
    remaining = dining_place.capacity - total_booked
    return Response({
        "place": dining_place.name,
        "total_capacity": dining_place.capacity,
        "remaining_capacity": remaining,
        "reservations": ReservationSerializer(reservations, many=True).data
    })

class MakeBookingView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
