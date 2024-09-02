from rest_framework import viewsets, status, generics
from rest_framework.views import APIView
from django.db.models import Count

from rest_framework.response import Response
from .models import Owner, Car, MaxCarsReachedException
from .serializers import OwnerSerializer, CarSerializer, CarSalesSerializer

class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except MaxCarsReachedException as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ProspectOwnerListView(generics.ListAPIView):
    queryset = Owner.objects.filter(is_prospect=True)
    serializer_class = OwnerSerializer

class MostSoldCarsView(APIView):
    def get(self, request):
        cars = Car.objects.values('model').annotate(count=Count('model')).order_by('-count')
        serializer = CarSalesSerializer(cars, many=True)
        return Response(serializer.data)