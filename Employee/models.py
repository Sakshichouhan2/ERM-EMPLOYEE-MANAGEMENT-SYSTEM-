from django.db import models

# Create your models here.
class PunchIn_PunchOut(models.Model):
    punch_in_time = models.DateTimeField()
    punch_out_time = models.DateTimeField()

class Notification(models.Model):
    notification = models.CharField(max_length=100)


class Leave(models.Model):
    employee_name =  models.CharField(max_length=50, null=True, blank=True)
    leave_application = models.CharField(max_length=200, null=True, blank=True)


class Attedence(models.Model):
    attendence = models.DateTimeField()


class Salary(models.Model):
    salary = models.CharField(max_length=500, null=True, blank=True)


class EOD(models.Model):
    eod = models.CharField(max_length=500)