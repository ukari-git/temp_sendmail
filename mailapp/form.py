from django import forms
from django.forms import Form
from .models import customer_models

class customer_form(forms.ModelForm):
    
    class Meta:
        model = customer_models