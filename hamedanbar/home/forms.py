from django import forms
from .models import Vakil

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Vakil
        fields = ('thumbnail',)