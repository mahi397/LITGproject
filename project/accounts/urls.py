from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('setgoals/', views.askGoals, name = 'setgoals'),
    path('mymood/', views.askMood, name = 'mymood'),
    path('myactivities/', views.askActivity, name = 'myactivities'),
]