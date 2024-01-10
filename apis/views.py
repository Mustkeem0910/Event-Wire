from rest_framework import viewsets
from .models import VenueTypes, Cities, VenueLogin, VendorTypes, VendorLogin
from .serializers import *
from .forms import *
from rest_framework import generics

class VenueTypesViewSet(viewsets.ModelViewSet):
    queryset = VenueTypes.objects.all()
    serializer_class = VenueTypesSerializer
    
class StatesViewSet(viewsets.ModelViewSet):
    queryset = States.objects.all()
    serializer_class = StatesSerializer

class CitiesViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitiesSerializer


class VendorTypesViewSet(viewsets.ModelViewSet):
    queryset = VendorTypes.objects.all()
    serializer_class = VendorTypesSerializer

class VenueLoginViewSet(viewsets.ModelViewSet):
    queryset = VenueLogin.objects.all()
    serializer_class = VenueLoginSerializer

class VendorLoginViewSet(viewsets.ModelViewSet):
    queryset = VendorLogin.objects.all()
    serializer_class = VendorLoginSerializer
    

class UserLoginViewSet(viewsets.ModelViewSet):
    queryset = UserLogin.objects.all()
    serializer_class = UserLoginSerializer
    
    
class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
    
# class VenueImageViewSet(viewsets.ModelViewSet):
#     queryset = VenueImage.objects.all()
#     serializer_class = VenueImageSerializer



class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer



class VendorTypesViewSet(viewsets.ModelViewSet):
    queryset = VendorTypes.objects.all()
    serializer_class = VendorTypesSerializer

    

from rest_framework.views import APIView    
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.http import JsonResponse



@api_view(['POST'])
def venue_login(request):
    return custom_user_login(request, VenueLogin, VenueLoginSerializer)

@api_view(['POST'])
def vendor_login(request):
    return custom_user_login(request, VendorLogin, VendorLoginSerializer)

def custom_user_login(request, model, serializer):
    if request.method == 'POST':
        user_name = request.data.get("user_name")
        password = request.data.get("password")

        try:
            user = model.objects.get(user_name=user_name)
        except model.DoesNotExist:
            user = None

        if not user:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if user and user.password == password:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            user_data = serializer(user).data
            return Response({'access_token': access_token, 'refresh_token': refresh_token, 'user': user_data}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Login failed'}, status=status.HTTP_401_UNAUTHORIZED)
        

class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        try:
            user = UserLogin.objects.get(email=email)
        except UserLogin.DoesNotExist:
            return Response({'detail': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        if user and user.password == password:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            # Include additional user data if needed
            user_data = {}  # Add user-related data here
            return Response({'access_token': access_token, 'refresh_token': refresh_token, 'user': user_data}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Login failed'}, status=status.HTTP_401_UNAUTHORIZED)
        

class VenueUploadView(APIView):
    def get(self, request, format=None):
        form = VenueForm()
        form_data = {
            'form_as_p': form.as_p,
            'fields': {
                'venue_type': form['venue_type'].value(),
                'name': form['name'].value(),
                'address': form['address'].value(),
                'rating': form['rating'].value(),
                'capacity': form['capacity'].value(),
                'image': form['image'].value(),
            }
        }
        return Response(form_data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        form = VenueForm(request.data)
        
        if form.is_valid():
            venue = form.save()
            serializer = VenueSerializer(venue)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'errors': form.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    

def get_venue_details(request):
    try:
        venues = Venue.objects.all()
        venue_data = [{
            'name': venue.name,
            'address': venue.address,
            'rating': str(venue.rating),
            'capacity': venue.capacity,
            'image': venue.image.url,
        } for venue in venues]
        return JsonResponse({'venues': venue_data})
    except Venue.DoesNotExist:
        return JsonResponse({'error': 'Venue not found'}, status=404)
