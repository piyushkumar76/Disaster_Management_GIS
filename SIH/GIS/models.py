from django.db import models



class Stations(models.Model):
    StationID = models.CharField(max_length=100,primary_key=True)
    StationName = models.CharField(max_length=1000)
    StationArea = models.CharField(max_length=1000)
    Latitude = models.CharField(max_length=50)
    Longitude = models.CharField(max_length=50)
    def __str__(self):
        return self.StationID

class Request(models.Model):
    RequestID = models.CharField(max_length=100, primary_key=True)
    IncidentType = models.CharField(max_length=200)
    image = models.CharField(max_length=50000)
    Latitude = models.CharField(max_length=50)
    Longitude = models.CharField(max_length=50)
    Details = models.CharField (max_length=1000, default="")
    def __str__(self):
        return self.RequestID


class ControlCenterLogIN(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=50)
    def __str__(self):
        return self.username
