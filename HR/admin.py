from django.contrib import admin
from .models import Login,Leave,Meeting,PunchIn_PunchOut, Employee_Details,EOD,Notification,Salary_Details,Add_Employee

# Register your models here.
admin.site.register(Login)
admin.site.register(Meeting)
admin.site.register(Leave)
admin.site.register(PunchIn_PunchOut)
admin.site.register(EOD)
admin.site.register(Notification)
admin.site.register(Salary_Details)
admin.site.register(Add_Employee)



