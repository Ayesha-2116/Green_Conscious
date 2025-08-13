from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)  # New field for event image
    location = models.CharField(max_length=255, default='Windsor, ON')
    category = models.ForeignKey('EventCategory', on_delete=models.CASCADE, related_name='events', default=1)

    def __str__(self):
        return self.name


class EventCategory(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True, null=False)
    #totalEvents = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    @property
    def total_events(self):
        return self.events.count()