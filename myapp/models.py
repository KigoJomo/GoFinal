from django.db import models

# Create your models here.

class Member(models.Model):
  fullName = models.CharField(max_length=100)
  email = models.EmailField()
  age = models.IntegerField()
  gender = models.CharField(max_length=50)
  yob = models.DateField()

  # def __str__(self):
  #   return self.fullName
  
class Product(models.Model):
  name = models.CharField(max_length=100)
  price = models.CharField(max_length=50)
  quantity = models.IntegerField()

  # def __str__(self):
  #   return f"{self.name} {self.quantity}"

class Appointment(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  phone = models.CharField(max_length=50)
  date = models.DateTimeField()
  department = models.CharField(max_length=50)
  doctor = models.CharField(max_length=100)
  message = models.TextField()

class Inquiry(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  subject = models.CharField(max_length=200)
  message = models.TextField()

  # def __str__(self):
  #   return self.name