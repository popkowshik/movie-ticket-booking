from django.urls import path
from . import views

urlpatterns = [
    path('',views.homeview,name='home'),
    path('booking_history/',views.booking_history_view,name='booking_history'),
    path('search_mv/',views.search_mv,name='search_mv')
]