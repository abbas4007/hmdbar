from django import forms
from .models import Vakil, Article


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Vakil
        fields = ('thumbnail',)


class VakilSearchForm(forms.ModelForm):
    class Meta:
        model = Vakil
        fields  = ('name',)

class ArticleSearchForm(forms.Form):
    title = forms.CharField(label="",widget = forms.TextInput( attrs = {'class' : 'form-control mt-2 p-1'}))

    # class Meta:
    #     model = Article
    #     fields  = ('title', )

class AdminContactForm(forms.Form):
    name = forms.CharField(label = "نام",widget=forms.TextInput(attrs={'class': 'form-control'}))
    lastname = forms.CharField(label = "نام خانوادگی",widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(label = "متن پیام",widget=forms.Textarea(attrs={'class': 'form-control'}))