from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import csv
import ast
import pandas as pd
from ast import literal_eval

from .forms import MoodForm
from .forms import GenreForm
from .forms import GoalForm

from .models import User
from .models import Mood
from .models import PrefGenre

from datetime import datetime

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username = username, password = raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def homepage(request):
    return render(request, 'home.html')

def askGoals(request):
    if request.method == 'POST':
        # POST, generate form with data from the request
        form = GoalForm(request.POST)
        # check if it's valid:
        if form.is_valid():
            # process data, insert into DB, generate email,etc
            goals = form.cleaned_data['goals']

            # redirect to a new url:
            return HttpResponseRedirect('/accounts/mymood')

    else:
        # GET, generate blank form
        form = GoalForm()
    return render(request, 'goalform.html', {'form': form})

def askMood(request):
    if request.method == 'POST':
        form = MoodForm(request.POST)
        if form.is_valid():
            mood = form.cleaned_data['mood']
            user = User.objects.get(pk=request.user.id)
            #store in db
            m = Mood(user = user, timestamp = datetime.now(), mood_entry = mood)
            m.save()
            return HttpResponseRedirect('/accounts/mygenres')
    else:
        form = MoodForm()
    return render(request, 'moodform.html', {'form': form})

def askGenre(request):                   
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            genre = form.cleaned_data['genre']
            user = User.objects.get(pk=request.user.id)
            mood = Mood.objects.latest('timestamp') 
            a = PrefGenre(user = user, timestamp = datetime.now(), genre = genre, mood = mood)
            a.save()
            return HttpResponseRedirect('/accounts/suggestionsforme')
    else:
        form = GenreForm()
    return render(request, 'genreform.html', {'form': form})


def suggestTodo(request):
    if(request.method == 'GET'):
        user = User.objects.get(pk=request.user.id)
        mood = Mood.objects.latest('timestamp')
        genre = PrefGenre.objects.latest('timestamp')

        if(mood == 'fine' or mood == 'great'):
            todo('fine', genre)
        else:
            todo('notsofine', genre)


def todo(moodclass, genre):
    path = r'C:\Users\HP\Desktop\LITG\LITGproject\project\accounts\genre_data.csv'
    with open(path,'r', encoding = 'utf-8') as csvfile:
        
        df = pd.read_csv(csvfile)
        col = df['genres'].apply(literal_eval)

        # print(type(col))
        # t = eval(col)
        for x in col:
            req_genre = x['name']
            print(req_genre)
        



def dashboard(request):
    return render(request, 'dashboard.html')



