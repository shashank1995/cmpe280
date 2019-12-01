from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import requests
import random
from .models import teams

# Create your views here.

def standings(request):
	if request.method == 'GET':

		context = {'result' : result}
		return render(request, 'sportscores/index.html', context)

def scores(request):
	if request.method == 'GET':
		all_teams = teams.objects.all()
		list_of_teams_used = []
		teams_to_be_displayed = []
		for a in range(10):
		#for a in range(1):
			print("Hello")
			print(a)
			flag = False
			while flag == False:
				random_number = random.randint(0,19)
				#random_number = random.randint(0,1)
				if random_number not in list_of_teams_used:
					print(random_number)
					team1 = teams.objects.get(team_id=random_number)
					list_of_teams_used.append(random_number)
					flag = True
			second_flag = False
			while second_flag == False:
				random_number = random.randint(0,19)
				#random_number = random.randint(0,1)
				if random_number not in list_of_teams_used:
					team2 = teams.objects.get(team_id=random_number)
					list_of_teams_used.append(random_number)
					second_flag = True
			team = {}
			team['team1_name'] = team1.teamName
			team['team1_url'] = team1.teamImage.url
			team['team2_name'] = team2.teamName
			team['team2_url'] = team2.teamImage.url
			team['team1_score'] = random.randint(0,6)
			team['team2_score'] = random.randint(0,6)
			teams_to_be_displayed.append(team)
		context = {'teams' : teams_to_be_displayed}
		return render(request, 'sportscores/scores.html', context)





