from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.conf import settings
from .models import CustomUser
from django.contrib.auth.forms import PasswordChangeForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="نام کاربری یا ایمیل", max_length=150,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری یا ایمیل'}))
    password = forms.CharField(label="رمز عبور",
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}))


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="رمز عبور", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="تکرار رمز عبور", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = CustomUser
        fields = ('phone',)


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise ValidationError("رمزهای عبور مطابقت ندارند.")
        validate_password(password2)
        return password2


class InitialBalance(forms.Form):
    amount = forms.IntegerField(
        label="مقدار دارایی (تومان)",
        min_value=0,
        widget=forms.NumberInput(attrs={'class': 'form-input'})
    )


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
        }


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-input'}))
