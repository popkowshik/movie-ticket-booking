from django.urls import path
from . import views
from dashboard import views as mv


urlpatterns = [
    path('register/',views.registerview,name='register'),
    path('login/',views.Login_view,name='login'),
    path('logout/',views.Logout_view,name='logout'),
    path('home/',mv.homeview,name='home'),
    path('identify/',views.IdentifyUserView,name='identify'),
    path('otp/<en_uname>/',views.otpview,name='otp'),
    path('reset_password/<en_uname>/',views.reset_password_view,name='reset_password'),
    path('update_password/',views.update_password,name='update_pwd')
]
