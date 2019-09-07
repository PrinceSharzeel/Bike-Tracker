from django import forms

class UploadCSV(forms.Form):
	vcsv = forms.FileField(label="CSV",widget=forms.FileInput(attrs={'required': 'yes'}))
