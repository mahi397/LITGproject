from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('home/', views.homepage, name = 'home'),
    path('setgoals/', views.askGoals, name = 'setgoals'),
    path('mymood/', views.askMood, name = 'mymood'),
    path('myactivities/', views.askActivity, name = 'myactivities'),
    path('mydashboard/', views.dashboard, name = 'mydashboard'),
]