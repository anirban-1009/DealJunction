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

# def send_otp_email(user):
#     otp = generate_otp()
#     user = User.objects.get(id=user.id)
#     user.email_otp = otp
#     user.save()

#     subject = 'OTP Verification'
#     message = f'Your OTP is: {otp}'
#     from_email = 'humanDensity009@gmail.com'
#     to_email = [user.email]

#     send_mail(subject, message, from_email, to_email)

def verify_otp(request):
    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            entered_otp = form.cleaned_data['otp']
            print(entered_otp)
            # Perform OTP verification logic here
            if entered_otp == '123456':  # Replace with your OTP verification logic
                return HttpResponse('OTP verification successful!')
            else:
                return HttpResponse('OTP verification failed!')
    else:
        form = OTPVerificationForm()
    return render(request, 'users/verify_otp.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email_verified = False
            user.save()
            
            #send_otp_email(user.id)
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {email}! Please verify your email.')
            return redirect('verify_otp')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})