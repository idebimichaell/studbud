from django.db import models
from django.contrib.auth.models import User
#from django.db.models.aggregates import Max
#from django.db.models.fields import UUIDField

# Create your models here. 

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 
    #id = UUIDField(primary_key=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

class Outline(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True)
    courseOutline = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    #id = models.UUIDField(primary_key=True)

    def __str__(self):
        return self.courseOutline

class Results(models.Model):
    topic = models.ForeignKey(Outline, on_delete=models.CASCADE, null=True)
    pdf = models.CharField(max_length=200)
    videos = models.CharField(max_length=200)

    def __str__(self):
        return self.pdf