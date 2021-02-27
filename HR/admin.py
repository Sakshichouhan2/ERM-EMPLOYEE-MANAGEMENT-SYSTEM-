from django.contrib import admin
from .models import Login,Employee_Registration,Leave,Meeting,PunchIn_PunchOut, Employee_Details,EOD,Notification,Salary_Details

# Register your models here.
admin.site.register(Login)
admin.site.register(Employee_Registration)
admin.site.register(Meeting)
admin.site.register(Leave)
admin.site.register(PunchIn_PunchOut)
admin.site.register(EOD)
admin.site.register(Notification)
admin.site.register(Salary_Details)




