from django.db import models





class Person(models.Model):
   firstname = models.CharField(max_length=100)
   lastname = models.CharField(max_length=10)
   nickname = models.CharField(max_length=10)
