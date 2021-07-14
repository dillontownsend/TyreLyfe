from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class CarGuy(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, validators=[EmailValidator()])
    car = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
