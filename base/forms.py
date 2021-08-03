from django import forms
from django.db import models
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self,  commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'



    # from_email = forms.EmailField(max_length=150)
    # subject = forms.CharField(max_length=50)
    # message = forms.CharField(widget=forms.Textarea, max_length=2000)

