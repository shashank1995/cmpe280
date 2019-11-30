# view.py

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import requests
from django.views.generic import TemplateView # Import TemplateView
from datetime import date, timedelta
import json

# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

class LoginPageView(TemplateView):
    template_name = "login.html"

def sportnews(request):
	if request.method == 'GET':
		# get today date
		today = date.today()
		# get yesterday time
		yesterday = today - timedelta(days = 1)

		sport_type = 'Soccer'
		sport_team = 'liverpool'

		sportnews_url = ("http://eventregistry.org/api/v1/article/getArticles?"
						"query=%7B%22%24query%22%3A%7B%22%24and%22%3A%5B%7B%22"
						"categoryUri%22%3A%22dmoz%2FSports%2F" + sport_type + "%22%7D%2C%7B%22"
						"dateStart%22%3A%22" + str(yesterday) + "%22%2C%22"
						"dateEnd%22%3A%22" + str(today) + "%22%2C%22lang%22%3A%22eng%22%7D%5D%7D%7D&dataType=news&resultType=articles&articlesSortBy=date&articlesCount=20&articleBodyLen=-1")
		
		print(sportnews_url)
		url_2 = "https://newsapi.org/v2/top-headlines?q=liverpool&category=sport&apiKey=379bb13707494380abacb61c130f8e2c"

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
		response = requests.request("GET", url_2)
		team_news = response.text
		context = {'result' : result, 'team_news' : team_news}
		return render(request, 'index.html', context)

def test_results(request):
	if request.method == 'GET':
		with open('static//test.json') as json_file:
			data = json.load(json_file)
		data = data['articles']['results']

		result = data

		context = {'result' : result}
		return render(request, 'test.html', context)
    	





