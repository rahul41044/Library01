from django.db import models

# Create your models here.
class Student(models.Model):
    book=models.CharField(max_length=100)
    author=models.CharField(max_length=100)
    issuedto=models.CharField(max_length=80)
    issueddate=models.CharField(max_length=50)
    # returndate=models.CharField(max_length=50,Required=FALSE)