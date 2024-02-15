from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=10, unique=True)
    # Add any other relevant fields

    designation = models.CharField(max_length=200)
    department = models.CharField(max_length=250)
    PAN = models.CharField(max_length=120)
    Account_number = models.CharField(max_length=20)
    

    # detection 1,2,3
    basic = models.FloatField()
    AGP = models.FloatField()
    Pay = models.FloatField()
    PP = models.FloatField()
    DA = models.FloatField()
    HRA = models.FloatField()
    Others = models.FloatField()

    gr_salary = models.IntegerField()

 # detetion 2 
    GPF = models.FloatField()

    GIS = models.FloatField()
    CPS = models.FloatField()
    PT = models.FloatField()
    IT = models.FloatField()
    LIC1 = models.FloatField()
    LIC2 = models.FloatField()

    deduction = models.IntegerField()
    # detction 3

    HR = models.FloatField()
    V_ADV = models.FloatField()
    AssocFee = models.FloatField()
    EHS_Empl_share = models.FloatField()
    Mar_Adv = models.FloatField()
    FC = models.FloatField()
    bFlaf_day_sub = models.FloatField()
    # net_salary = models.IntegerField()


    def __str__(self):
        return self.name




class Salary(models.Model):
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    month = models.CharField(max_length=20)
    year = models.PositiveIntegerField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    days = models.IntegerField()
    
    





class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name