from django import forms

class contactform(forms.Form):
    name  = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField(max_length=100)
    