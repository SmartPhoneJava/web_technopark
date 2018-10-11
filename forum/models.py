from django.db import models
from django.utils import timezone

from django.db import models
from django.utils import timezone


class User(models.Model):
    email = models.EmailField(max_length = 60)
    nickname = models.CharField(max_length = 20)
    password = models.CharField(max_length = 40)
    photo = models.ImageField(max_length=100)
    registration_date = models.DateTimeField(
           default=timezone.now)
    rating = models.IntegerField()

    def publish(self):
        self.registration_date = timezone.now()
        self.save()

    def __str__(self):
        return self.nickname
        
class Tag(models.Model):
    text = models.CharField(max_length = 40)
    
    def __str__(self):
        return self.text
        
class Question(models.Model):
    headline = models.TextField()
    content = models.TextField()
    author = models.ForeignKey('User', on_delete = models.CASCADE)
    created_date = models.DateTimeField(default = timezone.now)
    models.ForeignKey('Tag', on_delete = models.CASCADE)
    rating = models.IntegerField
    
    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.headline

class Answer(models.Model):
    content = models.TextField()
    author = models.ForeignKey('User', on_delete = models.CASCADE)
    created_date = models.DateTimeField(default = timezone.now)
    is_right = models.BooleanField()
    rating = models.IntegerField
    
    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.content