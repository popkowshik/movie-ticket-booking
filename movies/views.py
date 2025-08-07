from django.shortcuts import render, redirect
from .models import Movie,Cast
from reviews.models import Review
from django.db.models import Avg,Count,Sum
import datetime

# Create your views here.
def oneview(request,slug):
    movie = Movie.objects.get(slug=slug)
    cast = Cast.objects.filter(movie=movie)
    reviews = Review.objects.filter(movie=movie)
    rating = reviews.aggregate(avg = Avg('rating'))
    context = {
        'movie':movie,
        'cast':cast,
        'reviews':reviews,
        'rating':rating,
        'date':datetime.date.today()
    }
    return render(request,'movies/onemovie.html',context)

