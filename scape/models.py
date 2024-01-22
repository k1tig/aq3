from django.db import models
from django.contrib.auth.models import User
from catalog.models import TankSize, TankVolume, TankFilter, TankLight, TankCo2, TankSoil, TankHardscape
from fauna.models import Fish, Invertebrate
from flora.models import Plant
# Create your models here.

# Features: Add form for jounral update that has event options for "Add", "Remove", "Progress", "Rescape", ....



class Profile(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_profile")
    country = models.CharField(max_length=200)
    instagram = models.CharField(max_length=200)

    

class Scape(models.Model):
     name = models.CharField(max_length=200)
     owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
     size = models.ForeignKey(TankSize, on_delete=models.CASCADE)
     volume = models.ForeignKey(TankVolume, on_delete=models.CASCADE)
     filtration = models.ForeignKey(TankFilter, on_delete=models.CASCADE)
     lighting = models.ForeignKey(TankLight, on_delete=models.CASCADE)
     co2 = models.ForeignKey(TankCo2,on_delete=models.CASCADE)
     soil = models.ForeignKey(TankSoil, on_delete=models.CASCADE)
     hardscape = models.ManyToManyField(TankHardscape)

     
     plants = models.ManyToManyField(Plant, blank = True, related_name='scape_plants')
     fish = models.ManyToManyField(Fish, blank= True)
     invertebrates = models.ManyToManyField(Invertebrate, blank = True)

     def __str__(self): 
        return (self.name)