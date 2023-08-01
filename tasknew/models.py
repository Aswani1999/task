from django.db import models

# # Create your models here.
from django.db import models

class formmodel(models.Model):
    GENDER_CHOICES = (
         ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    ACCOUNT_TYPE_CHOICES = (
        ('Savings Account', 'Savings Account'),
        ('Current Account', 'Current Account'),
     )

    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    district = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    accountType = models.CharField(max_length=50, choices=ACCOUNT_TYPE_CHOICES)
    materials_provide = models.ManyToManyField('Material', blank=True)
    def __str__(self):
        return self.name

class material(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
