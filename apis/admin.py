from django.contrib import admin
from .models import Venue, VenueImage, Vendor, VendorImage

class VenueImageInline(admin.TabularInline):
    model = VenueImage
    extra = 1  # Number of empty forms to display for adding images

class VendorImageInline(admin.TabularInline):
    model = VendorImage
    extra = 1  # Number of empty forms to display for adding images

class VenueAdmin(admin.ModelAdmin):
    inlines = [VenueImageInline]

class VendorAdmin(admin.ModelAdmin):
    inlines = [VendorImageInline]

# Register the models with the admin site
admin.site.register(Venue, VenueAdmin)
admin.site.register(VenueImage)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(VendorImage)
