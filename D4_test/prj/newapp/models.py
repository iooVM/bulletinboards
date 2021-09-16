from django.db import models
from django.core.validators import MinValueValidator


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=128)  # имя товара
    description = models.TextField()
    quantity = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0, 'Quantity should be >= 0')])  # количество товара на складе
    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0, 'Quantity should be >= 0')])

    def __str__(self):
       return f'{self.name} {self.quantity}'


# категории товаров: именно на них ссылается модель товара
class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'

class Commenet(models.Model):
    text = models.TextField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'{self.text}'
