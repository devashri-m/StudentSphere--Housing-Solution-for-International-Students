from rest_framework import serializers
from .models import Comment
from apps.student.models import StudentModel
from apps.apartments.models import Apartment

class CommentSerializer(serializers.ModelSerializer):
    student_id = serializers.IntegerField(write_only=True)
    apartment_id = serializers.IntegerField(write_only=True)
    
    student_name = serializers.SerializerMethodField()
    apartment_name = serializers.SerializerMethodField()
    timestamp = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'student_id', 'student_name', 'apartment_id', 'apartment_name', 'timestamp']

   

    def get_student_name(self, obj):
        # Fetch the student name from the related Student object
        student = StudentModel.objects.get(id=obj.student_id)
        return f"{student.first_name} {student.last_name}" if student else None

    def get_apartment_name(self, obj):
        # Fetch the apartment name from the related Apartment object
        apartment = Apartment.objects.get(id=obj.apartment_id)
        return apartment.name if apartment else None

    
