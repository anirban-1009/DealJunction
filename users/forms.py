from django import forms
from django.core.exceptions import ValidationError

from .models import User

from django.contrib.auth.forms import UserCreationForm
# from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    
    class Meta:
        model = User
        fields = ['email',  'password1', 'password2']


class OTPVerificationForm(forms.Form):
    otp = forms.CharField(label='OTP', max_length=6)

    def clean_otp(self):
        otp = self.cleaned_data['otp']
        if not otp.isdigit() or len(otp) != 6:
            raise forms.ValidationError('Invalid OTP')
        return otp




class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Enter Password Again', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match

        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user