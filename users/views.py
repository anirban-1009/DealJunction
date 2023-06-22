from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, OTPVerificationForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from marketplace.models import Cart
from .models import User
import random
from django.http import HttpResponse
from django.core.mail import send_mail

def generate_otp(length=6):
    return ''.join(random.choices('0123456789', k=length))

def send_otp_email(email):
    otp = generate_otp()
    user = User.objects.get(email=email)
    user.email_otp = otp
    user.save()

    subject = 'OTP Verification'
    message = f'Your OTP is: {otp}'
    from_email = 'humanDensity009@gmail.com'
    to_email = [email]

    send_mail(subject, message, from_email, to_email)
    redirect('verify_otp', id=user.id)

def verify_otp(request, id):
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
    return render(request, 'users/verify_otp.html', {'form': form, 'id':id})


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