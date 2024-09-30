# forms.py
from django import forms
from home.models import Vakil


class ImageForm(forms.ModelForm):

    class Meta:
        model = Vakil
        fields = ['thumbnail']
