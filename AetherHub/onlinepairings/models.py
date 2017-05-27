from django.db import models
from django.utils import timezone

class Event(models.Model):
    Organizer = models.ForeignKey('auth.User')
    Title = models.CharField(max_length=100)
    Created_date = models.DateTimeField(default=timezone.now)
    WER_path = models.CharField(max_length = 300, default = 0)
    Current_round = models.CharField(max_length = 2, default = 0)

    def startevent(self):
        self.save()
    
    def __str__(self):
        return self.Title