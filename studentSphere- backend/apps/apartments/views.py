from rest_framework import generics
from .models import Apartment
from .serializers import ApartmentSerializer

class ApartmentList(generics.ListAPIView):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()

class ApartmentDetail(generics.RetrieveAPIView):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.all()
