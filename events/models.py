from django.db import models
from accounts.models import CustomUser
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    event_time = models.TimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    location = models.CharField(max_length=255)
    flyer = models.ImageField(upload_to='event_flyers/', blank=True, null=True)
    categories = models.ManyToManyField(Category, blank=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='events')

    def __str__(self):
        return self.name
