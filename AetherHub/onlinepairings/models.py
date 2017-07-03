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

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    current_round = models.CharField(max_length=2, default = 0)

class LookupField(models.Model):
    DCI_lookup = models.CharField(max_length=10, blank = True)
    Table_lookup = models.CharField(max_length=4, blank = True)

class Controls(models.Model):
    seatings = models.BooleanField(default = False)
    roundUpdate = models.CharField(max_length = 2)

class Player(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
   # currentOpp = models.CharField(max_length=75, default=0)
   # table = models.CharField(max_length=4, default=0)
    name = models.CharField(max_length=75)
    eventID = models.CharField(max_length = 20, default = 0)
    Otable = models.CharField(max_length=4, default=0)

    def __str__(self):
        return self.id
    def __repr__(self):
        return self.id

class Matches(models.Model):
    activePlayerID = models.CharField(max_length=10)
    opponentID = models.CharField(max_length=10)
    opponentName = models.CharField(max_length = 75)
    activePlayerWin = models.CharField(max_length=1, default = 0)
    opponentWin=models.CharField(max_length=1, default = 0)
    draws = models.CharField(max_length = 2, default = 0)
    eventID=models.CharField(max_length=10)
    roundNum=models.CharField(max_length=2)
    tableNum = models.CharField(max_length=4)
    byeCheck = models.CharField(max_length=1)

    def _get_compound_key(self):
        return self.eventID + self.numOfRound + self.activePlayerID

    compoundKey = property(_get_compound_key)