from django import forms
from .models import Vakil

class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Vakil
        fields = ('thumbnail',)


class VakilSearchForm(forms.ModelForm):
    class Meta:
        model = Vakil
        fields  = ('name',)