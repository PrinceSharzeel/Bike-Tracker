from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import *

class UploadCSV(forms.Form):
	vcsv = forms.FileField(label="CSV",widget=forms.FileInput(attrs={'required': 'yes'}))
