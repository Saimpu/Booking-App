from django.urls import path,include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns=[
    path('', views.api_root,name='api-root'),
    path('roomBooking/',views.RoomBooking.as_view(),name='room-list'),
    path('roomBooking/<int:pk>/',views.RoomDetails.as_view(),name='booking-detail'),
    path('occupied/',views.OccupiedDate1.as_view(),name='occupiedDteList-list'),
    path('occupied/<int:pk>/',views.OccupiedDate1Details.as_view(),name='occupieddate-detail'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
]

# urlpatterns=format_suffix_patterns(urlpatterns)

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

