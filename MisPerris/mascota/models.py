import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Mascota(models.Model):
    nombre = models.CharField(max_length=200, blank='true')
    raza = models.CharField(max_length=15)
    Descripcion = models.CharField(max_length=200)
    Estado = models.CharField(max_length=200)
    image = models.FileField(upload_to='images', blank='true')

    class Meta:
        db_table = u'mascota_question'

    def __str__(self):
        return self.Descripcion
    def get_absolute_url(self): 
    	return self.image
    

class Choice(models.Model):
    question = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

