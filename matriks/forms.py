from django.db import models
from django.contrib.auth.models import User
from . models import RCI
from django.forms import ModelForm

class RCICreate(ModelForm):
    class Meta:
        model = RCI
        fields = ['nama', 'parameter1', 'parameter2', 'parameter3']