from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from Employee import views

router=DefaultRouter()
router.register('PunchIn_PunchOut', views.PunchIn_PunchOutViewSet)
router.register('Notification', views.NotificationViewSet)
router.register('Leave', views.LeaveViewSet)
router.register('Attendence', views.AttendenceViewSet)
router.register('Salary', views.SalaryViewSet)
router.register('EOD', views.EODViewSet)

urlpatterns=[
    path("",include(router.urls)),
]

