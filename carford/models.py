from django.db import models
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError


class MaxCarsReachedException(ValidationError):
    pass

class Owner(models.Model):
    name = models.CharField(max_length=100, blank=False)
    is_prospect = models.BooleanField(default=True)
    qtd_cars = models.IntegerField(validators=[MaxValueValidator(3)])

    def __str__(self):
        return f"{self.name}"

    def update_prospect_status(self):
        self.is_prospect = self.qtd_cars == 0
        self.save()

    def save(self, *args, **kwargs):
        self.is_prospect = self.qtd_cars == 0
        super().save(*args, **kwargs)

class Car(models.Model):
    COLORS = [
        ('yellow', 'Yellow'),
        ('blue', 'Blue'),
        ('gray', 'Gray'),
    ]
    MODELS = [
        ('hatch', 'Hatch'),
        ('sedan', 'Sedan'),
        ('convertible', 'Convertible'),
    ]

    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    color = models.CharField(max_length=10, choices=COLORS)
    model = models.CharField(max_length=20, choices=MODELS)

    def __str__(self):
        return f"{self.color.name} : {self.model} - {self.color}"

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.owner.qtd_cars >= 3:
                raise MaxCarsReachedException("O proprietário já possui o número máximo de 3 carros.")

            self.owner.qtd_cars += 1
            self.owner.update_prospect_status()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.owner.qtd_cars -= 1
        self.owner.update_prospect_status()
        super().delete(*args, **kwargs)
