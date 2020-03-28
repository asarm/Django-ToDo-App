from django import forms
from django.forms import ModelForm
from .models import *


class InputForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter title'}), required=True)
    description = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter description'}), required=False)
    status = forms.BooleanField(required=False)

    class Meta:
        model = Task
        fields = '__all__'
