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


# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "registration/login.html"

class SignUp(generic.CreateView):
	form_class = UserCreationForm
	success_url = reverse_lazy('login')
	template_name = 'signup.html'

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
			return redirect('/redirect/')
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
			return redirect('/redirect/')
	else:
		profile = Profile.objects.get(user=user)
		form = ProfileForm(model_to_dict(profile))
	return render(request, 'profile.html', {'form': form})