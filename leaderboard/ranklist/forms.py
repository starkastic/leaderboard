from django import forms
from .models import Team

class teamform(forms.Form):
    player_11 = forms.CharField()
    player_21 = forms.CharField()
    player_12 = forms.CharField()
    player_22 = forms.CharField()
    score_1 = forms.IntegerField()
    score_2 = forms.IntegerField()
    #fields = ['player_11','player_12','player_21','player_22','score_1','score_2']
