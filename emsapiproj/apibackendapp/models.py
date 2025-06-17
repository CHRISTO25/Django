from django.db import models

class Department(models.Model):
    DepartmentId =models.AutoField(primary_key =True)
    DepartmentName =models.CharField(max_length=100)

    def _str_(self):
        return self.DepartmentName
       
class Employee (models.Model):
    EmployeeId = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Designation = models.CharField(max_length =100)
    DateOfJoining = models.DateField()
    DepartmentId= models.ForeignKey(Department,on_delete=models.CASCADE)
    Contact= models.CharField(max_length=15)
    IsActive= models.BooleanField(default=True)

    def __str__(self):
        return self.EmployeeName



    # ruxna3-pyzraM-niskeb