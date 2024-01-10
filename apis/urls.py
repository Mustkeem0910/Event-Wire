from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'venue-types', VenueTypesViewSet)
router.register(r'cities', CitiesViewSet)
router.register(r'states', StatesViewSet)
router.register(r'venue-logins', VenueLoginViewSet)
router.register(r'vendor-types', VendorTypesViewSet)
router.register(r'vendor-logins', VendorLoginViewSet)
router.register(r'user-logins', UserLoginViewSet)
router.register(r'venues', VenueViewSet)
# router.register(r'venue-images', VenueImageViewSet)
router.register(r'vendors', VendorViewSet)
router.register(r'vendor-types', VendorTypesViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('venue/login/', venue_login, name='venue_login'),
    path('vendor/login/', vendor_login, name='vendor_login'),
    path('user/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('upload_venue/', VenueUploadView.as_view(), name='upload_venue'),
    path('api/venues/', get_venue_details, name='get_venue_details'),
    # path('venue/', VenueCreateView.as_view(), name='venue'),
]
