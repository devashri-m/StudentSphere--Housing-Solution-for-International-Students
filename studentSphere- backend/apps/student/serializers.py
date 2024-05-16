from rest_framework import serializers
from apps.student.models import *


class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = '__all__'  

