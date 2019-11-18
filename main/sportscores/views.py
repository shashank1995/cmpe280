from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import requests

# Create your views here.

def standings(request):
	if request.method == 'GET':
		# url = "https://api-football-v1.p.rapidapi.com/v2/leagueTable/2"
		# headers = {
  #   		'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
  #   		#'x-rapidapi-key': "93116d6825mshc18d528f51f8096p19e99ajsnac9bd9278e8b"
  #   		'x-rapidapi-key': "8lxab1uReumsh14JwkQGRZTuv54jp1Oo6AhjsnJ7opghGVw9z3"
  #   	}
		# response = requests.request("GET", url, headers=headers)
		# print(response.text)
		url = "https://api-football-v1.p.rapidapi.com/v2/leagues/team/85"
		headers = {
    		'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    		'x-rapidapi-key': "8lxab1uReumsh14JwkQGRZTuv54jp1Oo6AhjsnJ7opghGVw9z3"
    	}
		response = requests.request("GET", url, headers=headers)
		print(response.text)
		print(response["api"]["standings"][0]["0"]["teamName"])
		result = response["api"]["standings"][0]["0"]["teamName"]
		context = {'result' : result}
		return render(request, 'sportscores/index.html', context)