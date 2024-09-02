from django.test import TestCase
from carford.models import Owner, Car
from carford.serializers import CarSerializer, CarSalesSerializer, OwnerSerializer

class SerializerOwnerTesteCase(TestCase):
    def setUp(self):
        self.owner = Owner(
            name="Test Name",
            qtd_cars=0,
        )

        self.serializer_owner = OwnerSerializer(instance=self.owner)


    def test_verify_fields_serializers_owner(self):
        data = self.serializer_owner.data
        self.assertEqual(set(data.keys()), set(['id','name','is_prospect','qtd_cars']))

    def test_content_fields_serializers_owner(self):
        data = self.serializer_owner.data

        self.assertEqual(data['name'], self.owner.name)
        self.assertEqual(data['qtd_cars'], self.owner.qtd_cars)
        self.assertEqual(data['is_prospect'], True)

class SerializerCarTestCase(TestCase):
    def setUp(self):
        self.owner = Owner.objects.create(
            name="Test Owner",
            qtd_cars=0,
        )

        self.car = Car.objects.create(
            owner=self.owner,
            color='blue',
            model='sedan',
        )

        self.serializer_car = CarSerializer(instance=self.car)

    def test_verify_fields_serializers_car(self):
        data = self.serializer_car.data
        self.assertEqual(set(data.keys()), set(['id', 'owner', 'color', 'model']))

    def test_content_fields_serializers_car(self):
        data = self.serializer_car.data

        self.assertEqual(data['owner'], self.car.owner.id)
        self.assertEqual(data['color'], self.car.color)
        self.assertEqual(data['model'], self.car.model)