import uuid
from django.db import models

# Create your models here.
class Doctor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    name = models.CharField(null=False, max_length=60) 
    specialization = models.CharField(null=False, max_length=60)
    number = models.CharField(unique=True, max_length=10)

class Slot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    start_time = models.TimeField()
    end_time = models.TimeField()

class Patient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    name = models.CharField(null=False, max_length=60)
    dob = models.DateField()
    age = models.IntegerField(default=0)
    gender = models.CharField(null= False, max_length=10)
    disease = models.CharField(max_length= 60)
    number = models.CharField(unique= True, max_length=10)

class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable= False)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    slod_id = models.ForeignKey(Slot, on_delete=models.CASCADE)
    slot_date = models.DateField()
    Is_booked = models.BooleanField()

