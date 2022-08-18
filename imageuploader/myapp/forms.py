from dataclasses import field
from operator import mod
from socket import fromshare
from django import forms
from .models import Image

class ImageForms(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        labels = {'photo':''}