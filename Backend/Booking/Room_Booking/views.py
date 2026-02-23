from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse 
from django.contrib.auth import authenticate
from rest_framework import permissions
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed,PermissionDenied
from .models import Booking,OccupiedDate,User
from django.contrib.auth import get_user_model
from .serializers import bookingSerializer,roomImagesSerializer,dateSerializer,UserSerializer

# Create your views here.
@api_view(['GET'])
def api_root(request,format=None):
    return Response({
        'roomBooking':reverse('room-list',request=request,format=format)
    })
class RoomBooking(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer 
    permission_classes = [IsAdminOrReadOnly]


class RoomDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = bookingSerializer
    permission_classes = [IsAdminOrReadOnly]
   
class OccupiedDate1(generics.ListCreateAPIView):
    queryset = OccupiedDate.objects.all()
    serializer_class = dateSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user=self.request.user
        if not user.is_superuser and not user.is_staff:
            return OccupiedDate.objects.filter(user=user)
        return super().get_queryset() 

class OccupiedDate1Details(generics.RetrieveUpdateDestroyAPIView):
    queryset = OccupiedDate.objects.all()
    serializer_class = dateSerializer
    permission_classes = [IsAdminOrReadOnly]
class UserList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user

        # Admin can see all users
        if user.is_staff or user.is_superuser:
            return User.objects.all()

        # Normal user sees only themselves
        return User.objects.filter(id=user.id)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        user = self.request.user
        obj = super().get_object()

        # Allow access if the user is fetching their own details or is an admin
        if obj == user or user.is_staff or user.is_superuser:
            return obj
        else:
            raise PermissionDenied("You do not have permission to access this user's details.")

class Register(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # Save the user
        user = serializer.save()

        # Generate token
        token, created = Token.objects.get_or_create(user=user)

        # Return user data and token in response
        self.response_data = {
            "user": {
                "id": user.id,
                "username": user.email,
                "email": user.email,
                "full_name":user.full_name
            },
            "token": token.key,
        }

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response(self.response_data)
    
        
    
class Login(APIView):
    def post(self, request, *args, **kwargs):
        # Extract username and password from the request data
        username = request.data.get('username')
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)

        if user is None:
            # Raise an error if authentication fails
            raise AuthenticationFailed('Invalid username or password')

        # Generate or retrieve the token
        token, created = Token.objects.get_or_create(user=user)

        # Return the user info and token
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "full_name":user.full_name
            },
            "token": token.key,
        })