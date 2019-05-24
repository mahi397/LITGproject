from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)


class Mood(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField()
    mood_entry = models.CharField()


class Activity(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField()
    activity = models.CharField()
    mood = models.ForeignKey(Mood)

