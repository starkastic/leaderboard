from django.shortcuts import render
from django.http import HttpResponse
from .models import Team
from django.template import loader
from .forms import teamform
from django import forms
from django.core.exceptions import ObjectDoesNotExist


def input(request):
    if request.method == 'POST':
        form = teamform(request.POST)
        if form.is_valid():
            template = loader.get_template('ranklist/input.html')
            try:
                team_1 = Team.objects.get(player_1 = request.POST['player_11'])
            except ObjectDoesNotExist:
                team_1 = Team(player_1 = request.POST['player_11'], player_2 = request.POST['player_21'])
            try:
                team_2 = Team.objects.get(player_1 = request.POST['player_12'])
            except ObjectDoesNotExist:
                team_2 = Team(player_1 = request.POST['player_12'], player_2 = request.POST['player_22'])
            score_1 = request.POST['score_1']
            score_2 = request.POST['score_2']
            if score_1 == score_2:
                #do nothing
            else if score_1 > score_2:
                team_1.score = team_1.score + 3
                team_2.score = team_2.score - 1
            else:
                team_1.score = team_1.score - 1
                team_2.score = team_2.score + 3
            team_1.save()
            team_2.save()
            return HttpResponse(template.render())
    else:
        form  = teamform
        return render(request, 'ranklist/input.html', {'form': form})



def display(request):
    top_ten_teams = Team.objects.all().order_by('score')[:10]
    template = loader.get_template('ranklist/display.html')
    context = {
        'top_ten_teams' : top_ten_teams,
    }
    return HttpResponse(template.render(context, request))
