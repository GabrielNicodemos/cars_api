from django.test import TestCase
from carford.models import Owner, Car

class ModelOwnerTestCase(TestCase):
    def setUp(self):
        self.owner_is_prospect = Owner.objects.create(
            name="João",
            qtd_cars=0,
        )

        self.owner_not_is_prospect = Owner.objects.create(
            name="José",
            qtd_cars=1,
        )

    def test_create_car_success(self):
        self.assertEqual(self.owner_is_prospect.name, 'João')
        self.assertEqual(self.owner_is_prospect.qtd_cars, 0)
        self.assertEqual(self.owner_is_prospect.is_prospect, True)

        self.assertEqual(self.owner_not_is_prospect.name, 'José')
        self.assertEqual(self.owner_not_is_prospect.qtd_cars, 1)
        self.assertEqual(self.owner_not_is_prospect.is_prospect, False)

class CarModelTest(TestCase):
    def setUp(self):
        self.owner = Owner.objects.create(name="Maria", qtd_cars=0)

    def test_create_car_success(self):
        car = Car.objects.create(owner=self.owner, color='blue', model='sedan')

        self.assertEqual(car.owner, self.owner)
        self.assertEqual(car.color, 'blue')
        self.assertEqual(car.model, 'sedan')
        self.assertEqual(self.owner.qtd_cars, 1)
        self.assertFalse(self.owner.is_prospect)