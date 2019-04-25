from django.db import models
from django.contrib.auth.models import User
from . models import RCI
from django import forms

class RCICreate(forms.ModelForm):
    class Meta:
        model = RCI
        fields = ['segmen', 'parameter1', 'parameter2', 'parameter3']

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

