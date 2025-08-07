from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from .forms import RegisterForm,LoginForm,IdentifyUserForm
from django.contrib.auth.forms import SetPasswordForm,PasswordChangeForm
from django.contrib import messages
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.conf import settings
from .models import User
from .utils import generate_otp, encode_uname, decode_uname
from django.utils import timezone
from datetime import timedelta

# Create your views here.

def registerview(request):
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            fname = form.cleaned_data['first_name']
            lname = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            send_mail(
                'Registration successfull',
                'hello' + fname + ' ' + lname + ', \n\nYou have successfully registered in movie ticket booking',
                'kowshikram2002@gmail.com',
                [email],
                fail_silently=True
            )
            return redirect('login')
    form = RegisterForm()
    context = {
        'form':form 
    }
    return render(request,'accounts/register.html',context)

def Login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                messages.success(request, f'Welcome, {user.username}!')
                return redirect('home')
        messages.error(request, 'Invalid username or password.')
        # return HttpResponse ('invalid user')
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def Logout_view(request):
    logout(request)
    messages.error(request, "You have been logged out")
    return redirect('home')
def Home_view(request):
    return render(request, 'accounts/home.html')

def IdentifyUserView(request):
    if request.method == 'POST':
        form = IdentifyUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                otp = generate_otp()
                time = timezone.now() + timedelta(minutes=10)
                user.otp_expiry = time
                user.otp = otp
                email = user.email
                user.save()
                send_mail(
                    'OTP for Movie Ticket Booking',
                    f'Your OTP is {otp}. It is valid for 10 minutes.',
                    'kowshikram2002@gmail.com',
                    [email],
                    fail_silently=False,
                )
                messages.success(request,'User found otp has sent to registered email')
                en_uname = encode_uname(user.username)
                url = f'/accounts/otp/{en_uname}/'
                return redirect(url)
            messages.error(request, 'User not found')
    
    form = IdentifyUserForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/identify.html', context)


def otpview(request, en_uname):
    username = decode_uname(en_uname)
    if User.objects.filter(username=username).exists():
        if request.method == 'POST':
            otp = int(request.POST.get('otp1') + request.POST.get('otp2') + request.POST.get('otp3') + request.POST.get('otp4'))
            user = User.objects.get(username=username)
            user.otp_verified = False
            if timezone.now() <= user.otp_expiry:
                if not user.otp_verified:
                    if otp == user.otp:
                        user.otp_verified = True
                        user.save()
                        messages.success(request, 'OTP verified successfully!')
                        url = f'/accounts/reset_password/{en_uname}/'
                        return redirect(url)
                    
                    url = f'/accounts/otp/{en_uname}/'
                    messages.error(request, 'Invalid OTP. Please try again.')
                    return redirect(url)
                messages.error(request, 'OTP already verified.')
                return redirect('otp', en_uname=en_uname) 
            messages.error(request, 'OTP expired. Please request a new OTP.')
            return redirect('identify')
        return render(request, 'accounts/otp.html')
    messages.error(request, 'Invalid Request')
    return redirect('login')


def reset_password_view(request, en_uname):
    dec_name = decode_uname(en_uname)
    user = User.objects.get(username=dec_name)
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            user.otp_verified = False
            user.otp = None
            user.otp_expiry = None
            user.save()
            messages.success(request, 'Password reset successfully!')
            return redirect('login')
        else:
            messages.error(request, 'Error resetting password. Please try again.')
    form = SetPasswordForm(user)
    context = {
        'form': form
    }
    return render(request, 'accounts/reset_password.html',context)

def update_password(request):
    user = User.objects.get(username = request.user.username)
    if request.method == 'POST':
        fm = PasswordChangeForm(user=user, data=request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'password update successful')
            return redirect('home')
        
    fm = PasswordChangeForm(user=user)
    context = {
        'form':fm
    }
    return render(request,'accounts/update_pwd.html',context)
