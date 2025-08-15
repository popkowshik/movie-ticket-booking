from django.shortcuts import render, redirect
from django.core.mail import send_mail
from theaters.models import Theater, Showtime, Seat
from movies.models import Movie
from accounts.models import User
from django.contrib import messages
from django.http import HttpResponse
import json
import datetime
from accounts.models import User
from django.contrib.auth.decorators import login_required
from .models import Booking,BookingSeat
from django.conf import settings
from django.views.decorators.http import require_POST

# List of dates (Today + next 5 days)
dates = [datetime.date.today() + datetime.timedelta(days=i) for i in range(6)]

def Theater_Showtime_view(request, slug, date_str=None):
    
    if not Movie.objects.filter(slug=slug).exists():
        messages.error(request, 'Movie not found')
        return redirect('movie_list')

    movie = Movie.objects.get(slug=slug)

    # If no date provided, default to today
    if date_str:
        selected_date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
    else:
        selected_date = datetime.date.today()

    current_time = datetime.datetime.now().time()
    theater_showtimes = []

    for theater in Theater.objects.all():
        if selected_date == datetime.date.today():
            shows = Showtime.objects.filter(
                movie=movie,
                theater=theater,
                showtime__date=selected_date,
                showtime__time__gte=current_time
            ).order_by('showtime')
        else:
            shows = Showtime.objects.filter(
                movie=movie,
                theater=theater,
                showtime__date=selected_date
            ).order_by('showtime')

        if shows.exists():
            theater_showtimes.append(shows)

    context = {
        'movie': movie,
        'theater_showtimes': theater_showtimes,
        'dates': dates,
        'slug': slug,
        'selected_date': selected_date
    }
    return render(request, 'theaters/theater_showtime.html', context)


def Seat_Selection_view(request, show_id):
    showtime_obj = Showtime.objects.get(id=show_id)
    theater = showtime_obj.theater
    movie = showtime_obj.movie
    seats = Seat.objects.filter(theater=theater).order_by('row_label', 'seat_number')

    seat_rows = {}
    booked_seats = [booking_seat.seat for booking_seat in BookingSeat.objects.filter(showtime=showtime_obj)]

    for seat in seats:
        row = (seat.row_label, seat.seat_type)
        if row not in seat_rows:
            seat_rows[row] = []
        if seat not in booked_seats:
            seat_rows[row].append(seat)
        else:
            seat_rows[row].append(0)

    context = {
        'movie': movie,
        'theater': theater,
        'showtime': showtime_obj,
        'seats': seats,
        'seat_rows': seat_rows,
    }
    return render(request, 'theaters/seatselection.html', context)

@login_required(login_url='login')
def Book_Ticket_View(request, show_id):
    showtime_obj = Showtime.objects.get(id=show_id)

    if request.method == 'POST':
        selected_seats = json.loads(request.POST['selected_seats'])
        total_amount = float(request.POST['total_amount'])
        tickets = []

        user = request.user

        convenience_fee = total_amount * 0.1
        sub_total = total_amount + convenience_fee

        booking = Booking.objects.create(
            user=user,
            showtime=showtime_obj,
            total_amount=sub_total
        )

        for seat in selected_seats:
            tickets.append(seat['key'])
            seat_id = seat['id']
            seat_obj = Seat.objects.get(id=seat_id)
            BookingSeat.objects.create(
                booking=booking,
                seat=seat_obj,
                showtime=showtime_obj
            )

        context = {
            'tickets': tickets,
            'sub_total': round(sub_total, 2),
            'convenience_fee': round(convenience_fee, 2),
            'total_amount': round(total_amount, 2),
            'showtime': showtime_obj,
            'booking':booking,
            'stripe_public_key':settings.STRIPE_PUBLIC_KEY,
        }
        return render(request, 'bookings/proceed_to_payment.html', context)

    return HttpResponse('Invalid Request')



@login_required
def cancel_ticket(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.status = 'cancelled'
    booking.save()
    qs = BookingSeat.objects.filter(booking=booking)
    qs.delete()
    booking.delete()
    messages.success(request,'Booking cancelled successfully')
    
    return redirect('booking_history')
