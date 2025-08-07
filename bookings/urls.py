from django.urls import path
from . import views

urlpatterns = [
    path('showtime/<slug>/<date_str>/',views.Theater_Showtime_view,name='theater_showtime'),
    path('seats/<int:show_id>/',views.Seat_Selection_view,name='seats'),
    path('seatbooking/<int:show_id>/',views.Book_Ticket_View,name='seatbooking'),
    path('cancel_booking/<int:booking_id>/',views.cancel_ticket,name='cancel_booking')
]