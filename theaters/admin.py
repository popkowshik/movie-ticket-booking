from django.contrib import admin
from .models import Theater,Seat,Showtime
# Register your models here.
@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Theater._meta.fields]

@admin.register(Seat)
class SeatAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Seat._meta.fields]

@admin.register(Showtime)
class ShowtimeAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Showtime._meta.fields]