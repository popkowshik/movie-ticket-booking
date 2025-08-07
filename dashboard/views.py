from django.shortcuts import render,redirect
from student.models import Movie
from bookings.models import Booking, BookingSeat
from payments.models import Payment
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def homeview(request):
    movies = Movie.objects.all()
    context = {
        'movies': movies
    }
    return render(request, 'movies/movies.html', context)


def search_mv(request):
    title = request.POST.get('title')
    try:
        movie = Movie.objects.get(title__iexact = title)
        context ={
            'movie':movie 
        }
        return render(request,'dashboard/search_mv.html',context)
    except:
        messages.error(request,'movie does not exist')
        return redirect('home')

@login_required(login_url='login')
def booking_history_view(request):
    """
    Fetch all bookings for the logged-in user, along with seats and payment details.
    """
    user_bookings = Booking.objects.filter(user=request.user).order_by('-booking_time')

    booking_data = []
    for booking in user_bookings:
        seats = BookingSeat.objects.filter(booking=booking)
        payment = Payment.objects.filter(booking=booking).first()
        
        booking_data.append({
            'booking': booking,
            'seats': seats,
            'payment': payment,
            'movie': booking.showtime.movie,   # Movie instance
            'theater': booking.showtime.theater,  # Theater instance
            'showtime': booking.showtime.showtime  # DateTime
        })

    context = {
        'booking_data': booking_data
    }
    return render(request, 'dashboard/booking_history.html', context)
