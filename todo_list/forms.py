from .models import list
from django import forms

class listform(forms.ModelForm):
    class Meta:
        model = list
        fields=['name','completed']
        