from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    liked_books = models.ManyToManyField(
        'Book', blank=True)  # Many-to-Many relationship

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()

    def __str__(self):
        return self.name
