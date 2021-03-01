from django.shortcuts import render
from . models import PunchIn_PunchOut, Notification, Leave,  Attendence, Salary, EOD
from rest_framework import viewsets
from Employee.Serializers import PunchIn_PunchOutSerializer, NotificationSerializer,  LeaveSerializer,  AttendenceSerializer, SalarySerializer, EODSerializer
 
# Create your views here.
class PunchIn_PunchOutViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PunchIn_PunchOut.objects.all()
    serializer_class = PunchIn_PunchOutSerializer



class NotificationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class LeaveViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer


class AttendenceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Attendence.objects.all()
    serializer_class = AttendenceSerializer

class SalaryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    

class EODViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = EOD.objects.all()
    serializer_class = EODSerializer


