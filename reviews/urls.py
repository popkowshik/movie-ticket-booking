from django.urls import path
from . import views

urlpatterns = [
    path('add_review/<slug>/',views.add_review_view,name='add_review'),
]