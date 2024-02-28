from django.db import models

class Flight(models.Model):
    airlines = models.CharField(max_length=100)
    departure_city = models.CharField(max_length=100)
    departure_airport = models.CharField(max_length=100, blank=True, null=True)
    arrival_airport = models.CharField(max_length=100, blank=True, null=True)
    destination_city = models.CharField(max_length=100)
    departure_date = models.DateTimeField(blank=True, null=True)
    arrival_date = models.DateTimeField()
    departure_time = models.TimeField(blank=True, null=True)
    arrival_time = models.TimeField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __str__(self):
        return f'{self.departure_city} to {self.destination_city}'

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __str__(self):
        return self.name

class Activity(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __str__(self):
        return self.name
    

class Package(models.Model):
    name = models.CharField(max_length=255)
    travel_duration = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    flight = models.ForeignKey(Flight, on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __str__(self):
        return self.name

class Booking(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.SET_NULL, null=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
    activity = models.ForeignKey(Activity, on_delete=models.SET_NULL, null=True)
    num_people = models.PositiveIntegerField(default=1)
    booking_description = models.TextField()
    booking_status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed')])
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
# class payment ()
#     Username:
#     booking id:
#     payment method 
#     Amout :



    
    
    
