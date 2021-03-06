from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
# class User(models.Model):
#     userid = models.AutoField(primary_key = True)
#     username = models.CharField(max_length = 20)
#     password = models.CharField(max_length = 20)


class Mood(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
# one user can have multiple moods, but one mood can only be connected to one user
    timestamp = models.DateTimeField(default = datetime.now)
    mood_entry = models.CharField(max_length = 20)
    def __unicode__(self):
        return self.description

'''
class Activity(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
# one user can have multiple activities, but one activity can only be connected to one user
    timestamp = models.DateTimeField(default = datetime.now)
    activity = models.CharField(max_length = 50)
    mood = models.ForeignKey(Mood, on_delete = models.CASCADE)
# one mood can be connected to multiple activities, but one activity can only be connected to one mood
'''

class PrefGenre(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
# one user can have multiple preferred genres, but one genre can only be connected to one user
    timestamp = models.DateTimeField(default = datetime.now)
    genre = models.CharField(max_length = 50)
    mood = models.ForeignKey(Mood, on_delete = models.CASCADE)
# one mood can be connected to multiple genres, but one genre can only be connected to one mood

    
