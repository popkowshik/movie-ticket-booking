from django.contrib import admin
from .models import Movie,Cast
# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # list_display = [
    #     'title', 'genre','language','synopsis','duration_minutes',
    #     'release_date','trailer_url','status','created_at','movie_image'
    # ]

    list_display = [field.name for field in Movie._meta.fields]

@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    # list_display = [
    #     'movie','name','role','image'
    # ]

    list_display = [field.name for field in Cast._meta.fields]
