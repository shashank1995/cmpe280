# account/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        fields = ('team')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        fields = ('team')