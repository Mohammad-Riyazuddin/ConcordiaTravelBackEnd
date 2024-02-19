from django.db import models

class Package(models.Model):
    name = models.CharField(max_length=255)
    travel_duration = models.CharField(max_length=255)
    description = models.TextField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class Flight(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='flights')
    airlines = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=100)
    destination_city = models.CharField(max_length=100)
    departure_date = models.DateField()
    return_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class Hotel(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='hotels')
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

class Activity(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='activities')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
