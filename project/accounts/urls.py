from django.urls import path

from . import views
    
urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('landing/', views.landing, name = 'landing'),
    path('home/', views.homepage, name = 'home'),
    path('setgoals/', views.askGoals, name = 'setgoals'),
    path('mymood/', views.askMood, name = 'mymood'),
    path('mygenres/', views.askGenre, name = 'mygenres'),
    path('mydashboard/', views.dashboard, name = 'mydashboard'),
    path('suggestionsforme/', views.suggestTodo, name = 'suggestionsforme'),
]