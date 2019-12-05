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
	('en', 'English'),
    ('es', 'Spanish')
)
class ProfileForm(forms.ModelForm):
	
	mysport = forms.ChoiceField(choices=SPORTS)
	myteam = forms.ChoiceField(choices=TEAMS)
	mylanguage = forms.ChoiceField(choices=LANGUAGES)
	class Meta:
		model = Profile
		fields = ['mysport', 'myteam', 'mylanguage']
    