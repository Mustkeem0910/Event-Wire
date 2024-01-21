from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from cloudinary import api
import cloudinary.uploader

# Create your models here.

class States(models.Model):
    """
    Represents different states.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'states'
    
    def __str__(self):
        return self.name


# Define the Cities Model    
# Modify the Cities model
class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    state = models.ForeignKey(States, related_name='cities', on_delete=models.CASCADE, default=1)
    image = CloudinaryField('image', null=True, blank=True)

    class Meta:
        db_table = 'cities'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Set the folder dynamically based on the venue's name
        folder_name = f'cities/{self.name}/'
        self.image.folder = folder_name

        # Save the image first to get the Cloudinary URL
        super(Cities, self).save(*args, **kwargs)

        # Update the image field with the Cloudinary URL
        self.image = self.image.url
        super(Cities, self).save(*args, **kwargs)

    
 
   

# Define the VenueLogin Model
class VenueLogin(models.Model):
    """
    Represents login information for a venue.
    """
    name = models.CharField(max_length=255, default="", blank=True)
    city = models.ForeignKey("Cities", on_delete=models.SET_NULL, null=True, blank=True)
    venue_type = models.ForeignKey("VenueTypes", on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(default="", blank=True)
    phone_number = models.CharField(max_length=20, default="", blank=True)
    user_name = models.CharField(max_length=255, unique=True, default="")
    password = models.CharField(max_length=255, default="")

    class Meta:
        db_table = 'venue_logins'

    def __str__(self):
        
        return self.user_name



class VendorLogin(models.Model):
    """
    Represents login information for a vendor.
    """
    name = models.CharField(max_length=255, default="", blank=True)
    city = models.ForeignKey("Cities", on_delete=models.SET_NULL, null=True, blank=True)
    vendor_type = models.ForeignKey("VendorTypes", on_delete=models.CASCADE, null=True, blank=True)
    email = models.EmailField(default="", blank=True)
    phone_number = models.CharField(max_length=20, default="", blank=True)
    user_name = models.CharField(max_length=255, unique=True, default="")
    password = models.CharField(max_length=255, default="")

    class Meta:
        db_table = 'vendor_logins'

    def __str__(self):
       
        return self.user_name
    
class UserLogin(models.Model):
    """
    Represents login information for a user.
    """
    name = models.CharField(max_length=255, default="", blank=True)
    email = models.EmailField(default="", blank=True)
    password = models.CharField(max_length=255, default="")
    event_city = models.ForeignKey("Cities", on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'user_logins'

    def __str__(self):
        return self.email
    

# Define the Venue Type Model
class VenueTypes(models.Model):
    """
    Represents different types of venues.
    """
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=255, default=None, null=True, blank=True)

    class Meta:
        db_table = 'venue_types'
        
    def __str__(self):
        return self.type

    
class Venue(models.Model):
    venue_type = models.ForeignKey("VenueTypes", on_delete=models.CASCADE, null=True, blank=True,related_name="venues")
    name = models.CharField(max_length=255, default="")
    address = models.CharField(max_length=255, default="")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    capacity = models.PositiveIntegerField(default=0)
    state = models.ForeignKey(States, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'venues'

    def __str__(self):
        return self.name

class VenueImage(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='venue_images')
    image = CloudinaryField('image')

    def save(self, *args, **kwargs):
        # Set the folder dynamically based on the venue's name
        folder_name = f'venues/{self.venue.name}/'
        self.image.folder = folder_name

        # Save the image first to get the Cloudinary URL
        super(VenueImage, self).save(*args, **kwargs)

        # Update the image field with the Cloudinary URL
        self.image = self.image.url
        super(VenueImage, self).save(*args, **kwargs)

    class Meta:
        db_table = 'venue_images'
        
    def __str__(self):
        return f"Image for {self.venue.name}"

    
    
# Define the Vendor type Model
class VendorTypes(models.Model):
    """
    Represents type of vendors.
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'vendor_types'
    
    def __str__(self):
        return self.name
 
 
class Vendor(models.Model):
    vendor_type = models.ForeignKey("VendorTypes", on_delete=models.CASCADE, null=True, blank=True, related_name="vendors")
    name = models.CharField(max_length=255, default="")
    address = models.CharField(max_length=255, default="")
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    charges = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    state = models.ForeignKey(States, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(Cities, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        db_table = 'vendors'

    def __str__(self):
        return self.name

class VendorImage(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, related_name='vendor_images')
    image = CloudinaryField('image')

    def save(self, *args, **kwargs):
        # Set the folder dynamically based on the vendor's name
        folder_name = f'vendors/{self.vendor.name}/'
        self.image.folder = folder_name

        # Save the image first to get the Cloudinary URL
        super(VendorImage, self).save(*args, **kwargs)

        # Update the image field with the Cloudinary URL
        self.image = self.image.url
        super(VendorImage, self).save(*args, **kwargs)

    class Meta:
        db_table = 'vendor_images'
        
    def __str__(self):
        return f"Image for {self.vendor.name}"   
    