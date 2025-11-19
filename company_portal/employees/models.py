from django.db import models

class Employee_records(models.Model):
    empid=models.IntegerField()
    empname=models.CharField(max_length=30)
    age=models.IntegerField()
    salary=models.IntegerField()
    designation=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
