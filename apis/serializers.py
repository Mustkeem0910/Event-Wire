from rest_framework import serializers
from .models import *



class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'
        
class StatesSerializer(serializers.ModelSerializer):
    cities = CitiesSerializer(many=True, read_only=True)

    class Meta:
        model = States
        fields = '__all__'

class VenueLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueLogin
        fields = '__all__'

class VendorTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorTypes
        fields = '__all__'

class VendorLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorLogin
        fields = '__all__'

class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogin
        fields = '__all__'


class VenueImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VenueImage
        fields = '__all__'


class VenueSerializer(serializers.ModelSerializer):
    venue_images = VenueImageSerializer(many=True, read_only=True)
    class Meta:
        model = Venue
        fields = ('id', 'name','state','city','address', 'rating', 'capacity', 'venue_images')
        
class VenueTypesSerializer(serializers.ModelSerializer):
    venues = VenueSerializer(many=True, read_only=True)

    class Meta:
        model = VenueTypes
        fields = ('id', 'type', 'venues')

class VendorImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorImage
        fields = '__all__'

class VendorSerializer(serializers.ModelSerializer):
    vendor_images = VendorImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Vendor
        fields = ('id', 'name','state','city', 'address', 'rating', 'charges', 'vendor_images')

class VendorTypesSerializer(serializers.ModelSerializer):
    vendors = VendorSerializer(many=True, read_only=True)

    class Meta:
        model = VendorTypes
        fields = ('id', 'name', 'vendors')
