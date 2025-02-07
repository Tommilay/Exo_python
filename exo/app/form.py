from django import forms
from app.models import Book

class contactform(forms.Form):
    name  = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=100)

class Bookform(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'