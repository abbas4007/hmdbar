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

class AdminContactForm(forms.Form):
    name = forms.CharField(label = "نام",widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(label = "نام خانوادگی",widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label = "متن پیام",widget=forms.Textarea(attrs={'class': 'form-control'}))