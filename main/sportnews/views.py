# view.py

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import requests
from django.views.generic import TemplateView # Import TemplateView
from datetime import date, timedelta
from accounts.models import Profile
import json

# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"

class LoginPageView(TemplateView):
    template_name = "login.html"

def sportnews(request):
	if request.method == 'GET':
		# get user info
		current_user = request.user
		current_profile = Profile.objects.get(user=current_user)
		sport_type = current_profile.mysport
		sport_team = current_profile.myteam
		language = current_profile.mylanguage
		print(sport_type)
		print(sport_team)

		# get today date
		today = date.today()
		# get yesterday time
		yesterday = today - timedelta(days = 1)

		sportnews_url = ("http://eventregistry.org/api/v1/article/getArticles?"
						"query=%7B%22%24query%22%3A%7B%22%24and%22%3A%5B%7B%22"
						"categoryUri%22%3A%22dmoz%2FSports%2F" + sport_type + "%22%7D%2C%7B%22"
						"dateStart%22%3A%22" + str(yesterday) + "%22%2C%22"
						"dateEnd%22%3A%22" + str(today) + "%22%2C%22lang%22%3A%22" + language + "%22%7D%5D%7D%7D&dataType=news&resultType=articles&articlesSortBy=date&articlesCount=10&articleBodyLen=-1")
		
		print(sportnews_url)
		sportteam_url = ("https://newsapi.org/v2/top-headlines?q=" + sport_team.lower() + "&category=sport"
						"&apiKey=379bb13707494380abacb61c130f8e2c")
		#url_2 = "https://newsapi.org/v2/top-headlines?q=liverpool&category=sport&apiKey=379bb13707494380abacb61c130f8e2c"

		response = requests.request("GET", sportnews_url)
		print(response.text)
		#print(response["api"]["standings"][0]["0"]["teamName"])
		data = response.text
		#data = "[" + data + "]"
		data = json.loads(data)
		data = data['articles']['results']
		#result = response.text
		result = data

		# get particular team new
		response = requests.request("GET", sportteam_url)
		team_news = response.text
		context = {'sport_type' : sport_type, 'result' : result, 'team_news' : team_news}
		return render(request, 'sportnews.html', context)

def test_results(request):
	if request.method == 'GET':
		current_user = request.user
		print(current_user.id)
		current_profile = Profile.objects.get(user=current_user)
		print(current_profile.mysport)

		with open('static//test.json') as json_file:
			data = json.load(json_file)
		data = data['articles']['results']

		result = data

		context = {'result' : result}
		return render(request, 'sportnews.html', context)
	else:
		current_user = request.user
		print(current_user.id)
		current_profile = Profile.objects.get(user=current_user)
		print(current_profile.mysport)

		with open('static//test.json') as json_file:
			data = json.load(json_file)
		data = data['articles']['results']

		result = data

		context = {'result' : result}
		return render(request, 'sportnews.html', context)
    	





