from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=256)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['name', 'client']

    def __str__(self):
        return self.name
