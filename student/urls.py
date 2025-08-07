from django.urls import path
from . import views 
urlpatterns = [
    path('onemovie/<slug>/',views.oneview,name='onemovie'),
]