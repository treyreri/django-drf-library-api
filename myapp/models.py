from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=2)
    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.ForeignKey( Country, on_delete=models.CASCADE )
    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    author = models.ForeignKey(Author,  on_delete=models.CASCADE )
    def __str__(self):
        return self.title