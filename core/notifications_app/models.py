from django.db import models
from patient_app.models import MedicalOrder
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
import datetime

# Create your models here.

class Notification(models.Model):
    initial_time= models.DateTimeField(blank=False, null=False)
    time_interval= models.DateTimeField() 
    repetitions= models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5)], blank=False, null=False)
    status= models.BooleanField(default=False)
    tittle = models.CharField(max_length=10,blank=False, null=False)
    description = models.CharField(max_length=100,blank=False, null=False)
    num_order= models.ForeignKey(MedicalOrder, on_delete=models.DO_NOTHING)
