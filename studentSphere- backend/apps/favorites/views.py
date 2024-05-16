# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from apps.apartments.models import Apartment
from apps.apartments.serializers import ApartmentSerializer

from apps.apartments.models import Apartment
from .models import Favorite
from .serializers import FavoriteSerializer

class FavoriteApartments(APIView):

    def post(self, request):
        student = request.user  
        apartment_id = request.data.get('apartment_id')

        try:
            favorite = Favorite.objects.get(student=student, apartment__id=apartment_id)
            return Response({'info': 'Apartment already in favorites'}, status=200)
        except Favorite.DoesNotExist:
            apartment = Apartment.objects.get(id=apartment_id)
            favorite = Favorite.objects.create(student=student, apartment=apartment)
            return Response({'success': 'Apartment added to favorites'}, status=201)
        except Apartment.DoesNotExist:
            return Response({'error': 'Apartment not found'}, status=400)

    def get(self, request):
        student = request.user
        favorites = Favorite.objects.filter(student=student)
        apartments = [favorite.apartment for favorite in favorites]  

        apartment_serializer = ApartmentSerializer(apartments, many=True)

        return Response({'apartments': apartment_serializer.data}, status=200)
    

    def delete(self, request):
        student = request.user
        apartment_id = request.data.get('apartment_id')

        try:
            favorite = Favorite.objects.get(student=student, apartment__id=apartment_id)
            favorite.delete()
            return Response({'success': 'Apartment removed from favorites'}, status=200)
        except Favorite.DoesNotExist:
            return Response({'info': 'Apartment not in favorites'}, status=200)
        except Apartment.DoesNotExist:
            return Response({'error': 'Apartment not found'}, status=400)