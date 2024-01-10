from django import forms
from .models import Venue

class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(),
        }