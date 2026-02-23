from rest_framework import serializers
from .models import Booking,RoomImages,OccupiedDate,User
class roomImagesSerializer(serializers.ModelSerializer):
    room = serializers.HyperlinkedRelatedField(
        view_name='booking-detail',
        queryset=Booking.objects.all()
    )
    class Meta:
        model = RoomImages
        fields = '__all__'

class dateSerializer(serializers.HyperlinkedModelSerializer):
    room = serializers.HyperlinkedRelatedField(
        view_name='booking-detail',
        queryset=Booking.objects.all()
    )
    user = serializers.HyperlinkedRelatedField(
        view_name='user-detail',
        queryset=User.objects.all()
    )
    class Meta:
        model = OccupiedDate
        fields = '__all__'



class bookingSerializer(serializers.HyperlinkedModelSerializer):
    occupiedDates = dateSerializer(many=True,read_only=True)
    images=roomImagesSerializer(many=True,read_only=True)
    class Meta:
        model = Booking
        fields =['url', 'id', 'name', 'types', 'pricepernight', 'currency', 'maxOccupency','occupiedDates','description','images']
        
from django.contrib.auth.hashers import make_password
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'id', 'username','password','email','full_name']

         
    def validate_password(self, value):
        return make_password(value)