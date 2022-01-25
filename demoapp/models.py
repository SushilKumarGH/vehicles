from django.db import models

VehicleType =[
    ("Bike", "Bike"),
    ("Car", "Car"),
    ("Zeep", "Zeep"),
    ("Bus", "Bus"),
    ("Truck", "Truck"),
]
EngineStatus=[
    ("Above Average","Above Average"),
    ("Average","Average"),
    ("Below Average","Below Average"),
]



# Create your models here.
class VehicleDetail(models.Model):
    Type = models.CharField(max_length=10, choices=VehicleType, default='None')
    Number = models.CharField(max_length=10)
    Status = models.BooleanField()
    Speed = models.FloatField()
    Averagespeed = models.FloatField()
    Temperature = models.FloatField()
    Fuellevel = models.FloatField()
    Enginestatus = models.CharField(max_length=20, choices=EngineStatus,default="None")
    def __str__(self):
        return self.Type