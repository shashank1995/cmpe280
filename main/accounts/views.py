# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView # Import TemplateView
from .forms import ProfileForm
from .models import Profile
from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate


# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "registration/login.html"

class AboutPageView(TemplateView):
	template_name = 'about.html'

class ContactPageView(TemplateView):
	template_name = 'contact.html'

class ServicesPageView(TemplateView):
	template_name = 'services.html'

class LandingPageView(TemplateView):
	template_name = 'index.html'

def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('profile')
	else:
		form = UserCreationForm()
	return render(request, 'signup.html', {'form': form})

'''
def login(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('profile')
	else:
		form = UserCreationForm()
	return render(request, 'login2.html', {'form': form})
'''	
def main_view(request):
	return render(request, 'main.html')

def add_profile(request):
	user = User.objects.get(id=request.user.id)
	if request.method == "POST":
		form = ProfileForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user

			post.save()
			return redirect('/landing/')
	else:
		form = ProfileForm()
	return render(request, 'profile.html', {'form': form})

def update_profile(request):
	user = User.objects.get(id=request.user.id)  
	instance = get_object_or_404(Profile, user=user)
	if request.method == "POST":
		form = ProfileForm(request.POST, instance=instance)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = request.user
			post.save()
			return redirect('/landing/')
	else:
		profile = Profile.objects.get(user=user)
		form = ProfileForm(model_to_dict(profile))
	return render(request, 'profile.html', {'form': form})