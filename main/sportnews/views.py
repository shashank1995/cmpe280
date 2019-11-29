# view.py

from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import requests
from django.views.generic import TemplateView # Import TemplateView

# Add the two views we have been talking about  all this time :)
class HomePageView(TemplateView):
    template_name = "index.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

class LoginPageView(TemplateView):
    template_name = "login.html"

def sportnews(request):
	if request.method == 'GET':
		sport_type = 'soccer'
		sport_team = 'liverpool'
		url = "http://eventregistry.org/api/v1/article/getArticles?query=%7B%22%24query%22%3A%7B%22%24and%22%3A%5B%7B%22categoryUri%22%3A%22dmoz%2FSports%2FSoccer%22%7D%2C%7B%22dateStart%22%3A%222019-11-25%22%2C%22dateEnd%22%3A%222019-11-26%22%2C%22lang%22%3A%22eng%22%7D%5D%7D%7D&dataType=news&resultType=articles&articlesSortBy=date&articlesCount=50&articleBodyLen=-1"
		
		url_2 = "https://newsapi.org/v2/top-headlines?q=liverpool&category=sport&apiKey=379bb13707494380abacb61c130f8e2c"

		response = requests.request("GET", url)
		print(response.text)
		#print(response["api"]["standings"][0]["0"]["teamName"])
		result = response.text

		# get particular team new
		response = requests.request("GET", url_2)
		team_news = response.text
		context = {'result' : result, 'team_news' : team_news}
		return render(request, 'index.html', context)