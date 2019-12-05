# account/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Profile

'''
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['mysport1', 'mysport2', 'myteam', 'language']
'''

SPORTS = (
	('', 'Choose...'),
    ('Soccer', 'Soccer'),
    ('Basketball', 'Basketball'),
    ('Football', 'Football'),
    ('Baseball', 'Baseball')
)

TEAMS = (
    ('', 'Choose...'),
	('Arsenal', 'Arsenal'),
    ('Liverpool', 'Liverpool'),
    ('Manchester United', 'Manchester United'),
    ('Norwich', 'Norwich')
)

LANGUAGES = (
    ('', 'Choose...'),
	('eng', 'English'),
    ('spa', 'Spanish')
)

GENDERS = (
    ('', 'Choose...'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)

class ProfileForm(forms.ModelForm):
    mysport = forms.ChoiceField(choices=SPORTS)
    myteam = forms.ChoiceField(choices=TEAMS)
    mylanguage = forms.ChoiceField(choices=LANGUAGES)
    mygender = forms.ChoiceField(choices=GENDERS)
    class Meta:
        model = Profile
        fields = ['myname', 'myage', 'mygender', 'mysport', 'myteam', 'mylanguage']
    