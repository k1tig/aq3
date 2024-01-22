from django.db import models

# Create your models here.
class Fish(models.Model):
     name = models.CharField(max_length=100)

     class Meta:
          verbose_name_plural =  "Fish"
     
     def __str__(self): 
        return self.name

class Invertebrate(models.Model):
     name = models.CharField(max_length=100)

     def __str__(self): 
        return self.name