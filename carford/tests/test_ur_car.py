from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from carford.models import Owner, Car
from carford.serializers import CarSerializer

class CarsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            password='admin'
        )

        self.client.force_authenticate(self.user)

        self.owner = Owner.objects.create(
            name="Test Owner",
            qtd_cars=1,
        )

        self.car1 = Car.objects.create(
            owner=self.owner,
            color="blue",
            model="sedan",
        )

        self.car2 = Car.objects.create(
            owner=self.owner,
            color="gray",
            model="hatch",
        )

        self.url = reverse('cars-list')

    def test_get_all_cars(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_by_id_car(self):
        response = self.client.get(f'{self.url}{self.car1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        car_data = Car.objects.get(pk=self.car1.id)
        car_data_serializers = CarSerializer(instance=car_data).data
        self.assertEqual(response.data, car_data_serializers)
