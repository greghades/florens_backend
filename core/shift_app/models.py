from django.db import models

# Create your models here.

class Shift(models.Model):
    id_shift= models.CharField(primary_key=True, max_length=10, null=False, unique=True)
    entry_time= models.DateTimeField()
    departure_time= models.DateTimeField()
    number_nurses= models.IntegerField()

    def __str__(self) -> str:
        return f'{self.id_shift} - {self.entry_time} - {self.departure_time} - {self.number_nurses}'