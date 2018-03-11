# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

from django.db import models

# Create your models here.
class userDetails(models.Model):
    id = models.AutoField(max_length=200, primary_key=True)
    fullName = models.CharField(max_length=200, blank=True, default="")
    sex = models.CharField(max_length=10)
    contact = models.CharField(max_length=12)
    email = models.CharField(max_length=100, blank=True)
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")
    registeredDate = models.DateTimeField(null=True)

    class Meta:
        db_table = 'userDetails'



class posts(models.Model):
    id = models.AutoField(max_length=200, primary_key=True)
    postText = models.TextField()
    postDate = models.DateTimeField()
    userDetailsId = models.ForeignKey(userDetails)
    likedCnt = models.IntegerField(default=0)
    dislikedCnt = models.IntegerField(default=0)

    class Meta:
        db_table = 'posts'