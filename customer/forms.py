from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from customer.models import CustomUser


class RegisterForm(UserCreationForm):
    username = forms.CharField(label="Foydalanuvchi nomi")
    full_name = forms.CharField(label="To‘liq ism")
    email = forms.EmailField(label="Email")

    password1 = forms.CharField(label="Parol", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Parolni tasdiqlang", widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Parollar mos kelmadi")

        return password2

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'email', 'password1', 'password2']




class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Login")
    password = forms.CharField(label="Parol", widget=forms.PasswordInput)