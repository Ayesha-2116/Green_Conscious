from django.db import models
from django.contrib.auth.models import User
from MainPage.models import *


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=50, blank=False, null=False)
    country = models.CharField(max_length=50, blank=False, null=False)
    profileImage = models.ImageField(upload_to='profile-images/', default=None, blank=True, null=True)
    eventInterested = models.ForeignKey(EventCategory, on_delete=models.CASCADE, default=1)


class SecurityQuestion(models.Model):
    question_text = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text


class SecurityAnswer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(SecurityQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.question.question_text}"