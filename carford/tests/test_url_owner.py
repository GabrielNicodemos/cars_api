from django.contrib.auth.models import User
from rest_framework.test import APITestCase, force_authenticate
from django.urls import reverse
from rest_framework import status
from carford.models import Owner, Car
from carford.serializers import OwnerSerializer

class OwnersTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='admin',
            password='admin'
        )

        self.url = reverse('owners-list')
        self.client.force_authenticate(self.user)

        self.owner1 = Owner.objects.create(
            name="Test Name 11",
            qtd_cars=0,
        )

        self.owner2 = Owner.objects.create(
            name="Test Name 222",
            qtd_cars=1,
        )

    def test_get_all_owner(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_by_id_owner(self):
        response = self.client.get(self.url+'1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        owner_data = Owner.objects.get(pk=1)
        owner_data_serializers = OwnerSerializer(instance=owner_data).data
        self.assertEqual(response.data, owner_data_serializers)