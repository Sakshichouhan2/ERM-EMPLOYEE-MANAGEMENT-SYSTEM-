from django.contrib import admin
from .models import PunchIn_PunchOut,Notification,Leave,Attedence,Salary,EOD

# Register your models here.
admin.site.register(PunchIn_PunchOut)
admin.site.register(Notification)
admin.site.register(Leave)
admin.site.register(Attedence)
admin.site.register(Salary)
admin.site.register(EOD)


