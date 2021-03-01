from .models import PunchIn_PunchOut, Notification, Leave,  Attendence, Salary, EOD
from rest_framework import serializers


class PunchIn_PunchOutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PunchIn_PunchOut
        fields = ['punch_in_time','punch_out_time']


class NotificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notification
        fields = ['notification']

class LeaveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Leave
        fields = ['id','employee_name','leave_application']

class AttendenceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Attendence
        fields = ['id','attendence']

class SalarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Salary
        fields = ['salary']

class EODSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = EOD
        fields = ['eod']
        