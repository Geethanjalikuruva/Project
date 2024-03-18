from typing import Any
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','password']
    def save(self):
        s=super().save(commit=False)
        s.password=make_password(self.cleaned_data['password'])
        s.save()
        return s

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


class patientForm(forms.ModelForm):
    class Meta:
        model=patientmodel
        fields="__all__"
    

class AppointmentForm(forms.Form):
    Full_Name = forms.CharField(max_length=100)
    doctor = forms.ModelChoiceField(queryset=docotrmodel.objects.all())
    service=forms.ModelChoiceField(queryset=servicesmodel.objects.all())
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))





