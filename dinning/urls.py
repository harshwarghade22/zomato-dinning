from django.urls import path
from .views import RegisterView, AddDiningPlaceView, search_dining_places, check_availability, MakeBookingView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('add-place/', AddDiningPlaceView.as_view(), name='add_place'),
    path('search/', search_dining_places, name='search'),
    path('availability/<int:pk>/', check_availability, name='availability'),
    path('book/', MakeBookingView.as_view(), name='book'),
]
