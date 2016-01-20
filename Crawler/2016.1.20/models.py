# coding:utf-8
from django.db import models


class Audio(models.Model):
    audioId = models.CharField(max_length=20, primary_key=True)
    audioTitle = models.CharField(max_length=100)
    audioType = models.CharField(max_length=20)
    audioDate = models.CharField(max_length=20, blank=True)
    audioUrl = models.CharField(max_length=100)
    audioImageUrl = models.CharField(max_length=100)
    audioLrcUrl = models.CharField(max_length=100)
    audioText = models.TextField()
    audioPartEndTime = models.CharField(max_length=50)
    audioTextBlankIndex = models.TextField(blank=True)
    avgCorrectRate = models.FloatField(max_length=10, blank=True)

    def __unicode__(self):
        return self.audioId


class User(models.Model):
    userId = models.CharField(max_length=50, primary_key=True)
    # userName = models.CharField(max_length=300)
    # userPassword = models.CharField(max_length=300)
    # userEmail = models.EmailField(blank=True)
    userWrongWords = models.TextField(blank=True)
    userCorrectRate = models.FloatField(max_length=10, blank=True)

    def __unicode__(self):
        return self.userId


class UserAudioBehavior(models.Model):
    audioId = models.ForeignKey(Audio, primary_key=True)
    userId = models.ForeignKey(User, primary_key=True)
    isCollected = models.BooleanField(default=False)
    userAnswer = models.TextField(blank=True)
    audioCorrectRate = models.FloatField(max_length=10, blank=True)

    def __unicode__(self):
        return self.audioId


class Words(models.Model):
    wordId = models.CharField(max_length=20,primary_key=True)
    word = models.CharField(max_length=50)
    audioIdList = models.TextField()

    def __unicode__(self):
        return self.word


