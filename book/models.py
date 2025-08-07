from django.db import models
from student.models import Movie
# Create your models here.
class Theater(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

seat_type_choices = [
    ('silver','silver'),
    ('gold','gold'),
    ('platinum','platinum')
]

class Seat(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    seat_number = models.IntegerField()
    row_label = models.CharField(max_length=1)
    seat_type = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.row_label} {self.seat_number}'
    
class Showtime(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    showtime = models.DateTimeField()
    silver_seats_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    gold_seats_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True) 
    platinum_seats_price = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  