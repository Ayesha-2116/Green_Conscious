# userhistory/models.py
from django.contrib.auth.models import User
from django.db import models


class UserHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.CharField(max_length=255)
    visit_count = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.path} - {self.date} - {self.visit_count}'
