from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .forms import MoodForm
from .forms import ActivityForm
from .forms import GoalForm

from .models import User
from .models import Mood
from .models import Activity

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
            m = Mood(user=user, timestamp = datetime.now(), mood_entry = mood)
            # m = Mood(
            #     user = get_user_model(),
            #     timestamp = datetime.now(),
            #     mood_entry = mood)
            m.save()
            return HttpResponseRedirect('/accounts/myactivities')
    else:
        form = MoodForm()
    return render(request, 'moodform.html', {'form': form})

def askActivity(request):
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.cleaned_data['activity']
            #store in db
            a = Activity(user = User(userid=login.user, username=login.username, password=login.raw_password),
                timestamp = datetime.now(),
                activity = activity,
                mood = Mood.mood_entry)
            a.save()
            return HttpResponseRedirect('/accounts/mydashboard')
    else:
        form = ActivityForm()
    return render(request, 'activityform.html', {'form': form})

def dashboard(request):
    return render(request, 'dashboard.html')
