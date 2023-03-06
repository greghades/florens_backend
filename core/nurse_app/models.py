from django.db import models
from authentication.models import NursUser
from patient_app.models import PatientUser, MedicalOrder
from medicine_app.models import Medicine
from django.core.validators import MinValueValidator
from django.utils import timezone
import datetime
# Create your models here.

class Report(models.Model):
    report_number = models.CharField(max_length=10,primary_key=True,null=False, unique=True)
    date = models.DateTimeField(auto_now=True,blank=False, null=False)
    description= models.CharField(max_length=300, blank=False, null=False)
    ine_nurs= models.ForeignKey(NursUser, on_delete=models.CASCADE)
    ine_patient= models.ForeignKey(PatientUser, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.report_number} - {self.description}'

class InputRequest(models.Model):
    application_number= models.CharField(primary_key=True, max_length=20, null=False, unique=True)
    date= models.DateTimeField(auto_now=True,blank=False, null=False)
    note= models.CharField(max_length=300, blank=False, null=False)
    ine_nurs= models.ForeignKey(NursUser, on_delete=models.CASCADE)
    #durg_code > hereda de app medicina
    durg_code= models.ForeignKey(Medicine, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.application_number} - {self.note} - {self.ine_nurs}'
        
class AttentionOrder(models.Model):
    num_attention= models.CharField(primary_key=True, max_length=5, null=False, unique=True)
    attention_time= models.DateTimeField(auto_now=True,blank=False, null=False)
    completed_by= models.CharField(max_length=100,blank=False, null=False)
    note= models.CharField(max_length=100,blank=False, null=False)
    num_order= models.ForeignKey(MedicalOrder, on_delete=models.DO_NOTHING)

class WorkStation(models.Model):
    id_workstation = models.CharField(primary_key=True, max_length=20, null=False, unique=True)
    name = models.CharField(max_length=10,null=False,blank=False)

class Nurse_WorkStation(models.Model):
    id_nurs_workstation = models.CharField(primary_key=True, max_length=20, null=False, unique=True)
    id_workstation = models.ForeignKey(WorkStation,on_delete=models.CASCADE)
    ine_nurs= models.ForeignKey(NursUser, on_delete=models.CASCADE)
