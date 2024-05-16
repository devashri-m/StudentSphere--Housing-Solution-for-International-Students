from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Q

from apps.student.serializers import studentSerializer  
from apps.student.models import StudentModel
from apps.utils import WriteErrorLogs  


class StudentLogin(APIView):
    authentication_classes = []  
    permission_classes = [AllowAny]
    serializer_class = studentSerializer  

    def post(self, request):
        try:
            request_data = request.data

            email = request_data['email']
            password = request_data['password']

            user = authenticate(request, username=email, password=password)
            print("Received data:", user)  

            if user:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)

                return Response({
                    'Success': True,
                    'Message': 'Login Successful',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }, status=200)
            else:
                return Response({'Success': False, 'Message': 'Invalid credentials'}, status=400)

        except Exception as err:
            return Response({'Success': False, 'Error': str(err)}, status=400)

class StudentLogout(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            logout(request)
            return Response({'Success': True, 'Message': 'Logged out successfully'}, status=status.HTTP_200_OK)

        except Exception as err:
            return Response({'Success': False, 'Error': str(err)}, status=status.HTTP_400_BAD_REQUEST)
class StudentCRUD(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def get(self, request, id=None):
        success = False

        try:
            search_query = request.GET.get('search', '')

            # Filter students based on search query
            if search_query:
                students = StudentModel.objects.filter(
                    Q(first_name__icontains=search_query) |  
                    Q(last_name__icontains=search_query) |   
                    Q(college__icontains=search_query) |     
                    Q(apartment__icontains=search_query),   
                    active=True
                )
            else:
                students = StudentModel.objects.filter(active=True)

            serializer = studentSerializer(students, many=True)
            success = True
            return Response({'Success': success, 'Message': serializer.data}, status=200)

        except Exception as err:
            WriteErrorLogs('StudentCRUD', 'get', str(request.data), str(err))
            return Response({'Success': success, 'Error': str(err)}, status=400)

    def post(self, request):
        success = False

        try:
            serializer = studentSerializer(data=request.data)

            if serializer.is_valid():
                user = serializer.save()
                user.set_password(request.data['password'])
                user.save()

                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                refresh_token = str(refresh)

                success = True

                return Response({
                    'Success': success,
                    'Message': 'User registered successfully',
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }, status=status.HTTP_201_CREATED)
            else:
                return Response({'Success': success, 'Error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            print("Exception details:", str(err))  

            return Response({'Success': success, 'Error': str(err)}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        success = False

        try:
            user_obj = StudentModel.objects.get(id=request.data['id'])

            serializer = studentSerializer(user_obj, data=request.data, partial=True)

            if serializer.is_valid():
                serializer.save()
                success = True
                return Response({'Success': success, 'Message': 'Updated Successfully'}, status=200)
            else:
                return Response({'Success': success, 'Error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            WriteErrorLogs('StudentCRUD', 'patch', str(request.data), str(err))
            return Response({'Success': success, 'Error': str(err)}, status=400)

    def delete(self, request):
        success = False

        try:
            user_id = request.data.get('id')
            user = StudentModel.objects.get(id=user_id)

            user.active = False
            user.save()

            success = True
            return Response({'Success': success, 'Message': 'Deleted'}, status=200)

        except Exception as err:
            WriteErrorLogs('StudentCRUD', 'delete', str(request.data), str(err))
            return Response({'Success': success, 'Error': str(err)}, status=400)
