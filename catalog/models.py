from django.db import models




class TankSize(models.Model):
     size =  models.CharField(max_length=10)

     def __str__(self): 
        return self.size

class TankVolume(models.Model):
     volume = models.CharField(max_length=10)

     class Meta:
          verbose_name_plural = "Tank volume"

     def __str__(self): 
        return self.volume

class TankFilter(models.Model):
     filter =  models.CharField(max_length=200)

     def __str__(self): 
        return self.filter

class TankLight(models.Model):
     light = models.CharField(max_length=200)

     def __str__(self): 
        return self.light

class TankCo2(models.Model):
     co2 = models.CharField(max_length=5)

     class Meta:
          verbose_name_plural = "co2"
     def __str__(self): 
        return self.co2

class TankSoil(models.Model):
     soil = models.CharField(max_length=100)

     def __str__(self): 
        return self.soil

class TankHardscape(models.Model):
     HARDSCAPE_TYPES = [
         ("S" , "Stone"),
         ("W", "Wood"),
     ]
     hardscape = models.CharField(max_length=100)
     hardscape_type = models.CharField(choices = HARDSCAPE_TYPES, max_length=10)

     def __str__(self):
         return self.hardscape


