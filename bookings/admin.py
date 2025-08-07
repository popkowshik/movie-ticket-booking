from django.contrib import admin
from .models import Booking,BookingSeat
# Register your models here.

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = [field.name for field in Booking._meta.fields]

@admin.register(BookingSeat)
class BookingSeatAdmin(admin.ModelAdmin):

    list_display = [field.name for field in BookingSeat._meta.fields]