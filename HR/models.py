from django.db import models
import datetime

# Create your models here.
#HR Registration
class Login(models.Model):
    username = models.CharField(max_length=50, null=True, blank=True)
    password = models.CharField(max_length=50)


#Employee Registration
'''
Hr Functionality-
1.Employee Details
2. Employee new registration
3.leave application
4.meeting
5.Attedennce
6.PunchIn PunchOut(BreakTime)
7.EOD
8.Notification
9.Salary Details(Pay slip-- if anyone want)
'''

class Add_Employee(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=70, blank=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    username = models.CharField(max_length=50, null=True, blank=True) 
    Address = models.CharField(max_length=200, null=True, blank=True)

'''
    class Employee_Registration(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=70,blank=True)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    
'''


class Meeting(models.Model):
    meeting = models.CharField(max_length=500, null=True, blank=True)



class Attedence(models.Model):
    id = models.AutoField(primary_key=True)
    attendence = models.DateTimeField()



class PunchIn_PunchOut(models.Model):
    punch_in_time = models.DateTimeField()
    punch_out_time = models.DateTimeField()



class Employee_Details(models.Model):
    employee_name = models.CharField(max_length=100)
    Profile = models.CharField(max_length=100)
    

class EOD(models.Model):
    eod = models.CharField(max_length=500)



class Notification(models.Model):
    notification = models.CharField(max_length=100)



class Salary_Details(models.Model):
    salary = models.CharField(max_length=500, null=True, blank=True)
    #if anyone want salary details
 

class Leave(models.Model):
    id = models.AutoField(primary_key=True)
    Employee_id =  models.IntegerField()
    Employee_Name = models.CharField(max_length=100, null=True, blank=True)
    Leave_Date = models.DateTimeField()
    Leave_Message = models.CharField(max_length=200, null=True, blank=True)
    Apply_On = models.DateTimeField()
    Action = models.CharField(max_length=100, null=True, blank=True)



