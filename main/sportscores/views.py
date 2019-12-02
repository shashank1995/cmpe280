from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import requests
import random
from .models import teams

# Create your views here.

def scores(request):
	if request.method == 'GET':
		all_teams = teams.objects.all()
		list_of_teams_used = []
		teams_to_be_displayed = []
		for a in range(10):
			flag = False
			while flag == False:
				random_number = random.randint(0,19)
				if random_number not in list_of_teams_used:
					team1 = teams.objects.get(team_id=random_number)
					list_of_teams_used.append(random_number)
					flag = True
			second_flag = False
			while second_flag == False:
				random_number = random.randint(0,19)
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


def predictor(request):
	if request.method == 'GET':
		all_teams = teams.objects.all()
		context = {'all_teams' : all_teams}
		return render(request, 'sportscores/predictor.html', context)
	if request.method == 'POST':
		team1 = request.POST.get('team1')
		team2 = request.POST.get('team2')
		team_rankings = ['Liverpool','Manchester City','Chelsea','Arsenal','Tottenham Hotspur','Manchester United','Leicester City','Everton',
		'Wolverhampton Wanderers','Sheffield United','Burnley','Crystal Palace','AFC Bournemouth','West Ham United','Newcastle United','Aston Villa',
		'Brighton and Hove Albion','Southampton','Norwich City','Watford']
		team1_index = team_rankings.index(team1)
		team2_index = team_rankings.index(team2)
		team_winning_confidence_score = str(random.randint(30,90)) + "%" 
		if team1_index <= team2_index:
			team_winner_predictor = team1
		else:
			team_winner_predictor = team2
		context = { 'team_winner_predictor' : team_winner_predictor, 'team_winning_confidence_score' : team_winning_confidence_score }
		return render(request, 'sportscores/predictorWinner.html', context)



