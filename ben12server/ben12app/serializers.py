from rest_framework import serializers
from .models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ["id", "name", "date_of_birth", "date_created", "last_measurement", "last_time_alcohol_consumed",
                  "address", "should_test_alcohol"]


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ["client", "heartbeat", "blood_oxygen_level", "alcohol_level", "date_time_recording", "date_time_sent"]


class DayAverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningAverageDay
        fields = ["client", "heartbeat", "blood_oxygen_level", "alcohol_level", "num_records", "date_last_updated"]


class MonthAverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningAverageMonth
        fields = ["client", "heartbeat", "blood_oxygen_level", "alcohol_level", "num_records", "date_last_updated"]


class WeekAverageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RunningAverageWeek
        fields = ["client", "heartbeat", "blood_oxygen_level", "alcohol_level", "num_records", "date_last_updated"]