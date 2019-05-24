from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)


class Mood(models.Model):
    user = models.ForeignKey(User)
# one user can have multiple moods, but one mood can only be connected to one user
    timestamp = models.DateTimeField()
    mood_entry = models.CharField()


class Activity(models.Model):
    user = models.ForeignKey(User)
# one user can have multiple activities, but one activity can only be connected to one user
    timestamp = models.DateTimeField()
    activity = models.CharField()
    mood = models.ForeignKey(Mood) 
# one mood can be connected to multiple activities, but one activity can only be connected to one mood

