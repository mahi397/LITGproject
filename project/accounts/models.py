from django.db import models

# Create your models here.
class User(models.Model):
    userid = models.AutoField(primary_key = True)
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)


class Mood(models.Model):
    userid = models.IntegerField(primary_key = True)
    timestamp = models.DateTimeField(primary_key = True)
    mood_entry = models.CharField()


class Acitivity(models.Model):
    userid = models.IntegerField(primary_key = True)
    timestamp = models.DateTimeField(primary_key = True)
    activity = models.CharField()
