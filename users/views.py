from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, OTPVerificationForm
from .models import User
import random
from django.http import HttpResponse
from django.core.mail import send_mail
from django_auth.secret import EMAIL


def generate_otp(length=6):
    return ''.join(random.choices('0123456789', k=length))

def send_otp_email(email):
    otp = generate_otp()
    user = User.objects.get(email=email)
    user.email_otp = otp
    user.save()

    subject = 'OTP Verification'
    message = f'Your OTP is: {otp}'
    from_email = EMAIL
    to_email = [email]

    send_mail(subject, message, from_email, to_email)
    redirect('verify_otp', id=user.id)

def verify_otp(request, id):
    user = User.objects.get(id=id)
    mail = user.email
    print(mail)
    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            user = User.objects.get(id=id)
            u_otp = user.email_otp
            # Perform OTP verification logic here
            if entered_otp == u_otp:  # Replace with your OTP verification logic
                user.email_verified = True
                user.save()
                return redirect('home')
            else:
                return HttpResponse('OTP verification failed!')
    else:
        form = OTPVerificationForm()
    return render(request, 'users/verify_otp.html', {'form': form, 'id':id, 'mail': mail})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email_verified = False
            user.save()
            email = form.cleaned_data.get('email')
            user = User.objects.get(email=email)
            send_otp_email(email)
            messages.success(request, f'Account created for {email}! Please verify your email.')
            return redirect('verify_otp', id=user.id)
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login_and_email_verified_required(view_func):
    """
    Custom decorator to require both login and email verification.
    """
    @login_required
    def wrapper(request, *args, **kwargs):
        if request.user.email_verified:
            # User is logged in and email is verified
            return view_func(request, *args, **kwargs)
        else:
            # Redirect to email verification page
            return redirect('verify_otp', id=request.user.id)
    
    return wrapper