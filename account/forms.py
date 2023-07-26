# Import all requirements
from django.contrib.auth import authenticate, login as DjangoLogin
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import UserChangeForm, ReadOnlyPasswordHashField
from django.contrib.auth.forms import UsernameField
from .models import user_accounts
from django.db.models import Q
from django.db import models
from django import forms


class LoginForm(AuthenticationForm):
    codeMelli = forms.CharField(
        label='کد ملی',
        widget=forms.TextInput(attrs={'placeholder': 'کد ملی'})
    )

    def clean(self):
        email = self.cleaned_data.get('email')
        codeMelli = self.cleaned_data.get('codeMelli')
        password = self.cleaned_data.get('password')

        if email and password and codeMelli:
            user = authenticate(request=self.request, username=email, codeMelli=codeMelli, password=password)
            if user is None:
                raise forms.ValidationError('اطلاعات وارد شده صحیح نیست')
            else:
                self.confirm_login_allowed(user)

        return self.cleaned_data


class CustomUserCreationForm(forms.ModelForm):
    email = forms.CharField(
        label='ایمیل',
        widget=forms.TextInput(attrs={'placeholder': 'ایمیل اپراتور انبار را وارد کنید'})
    )
    codeMelli = forms.CharField(
        label='کد ملی',
        widget=forms.TextInput(attrs={'placeholder': 'کد ملی اپراتور را وارد کنید'})
    )
    password1 = forms.CharField(
        label='رمز عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'رمز عبور'})
    )
    password2 = forms.CharField(
        label='تکرار رمز عبور',
        widget=forms.PasswordInput(attrs={'placeholder': 'تکرار رمز عبور'})
    )

    def clean_email(self):
        email = self.cleaned_data.get("email")

        return email


    class Meta:
        model = user_accounts
        fields = ('email', 'codeMelli', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("رمز عبور وارد شده مطابقت ندارند")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    email = forms.EmailField(label='ایمیل')
    first_name = forms.CharField(label='نام')
    last_name = forms.CharField(label='نام خانوادگی')
    codeMelli = forms.CharField(label='کد ملی')
    phoneNumber = forms.CharField(label='شماره تماس')
    is_active = forms.BooleanField(label='فعال', required=False)
    is_staff = forms.BooleanField(label='کارمند', required=False)
    date_joined = forms.DateTimeField(label='تاریخ عضویت', widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = user_accounts
        fields = ('email', 'first_name', 'last_name', 'codeMelli', 'phoneNumber', 'is_active', 'is_staff', 'date_joined')

    def clean_password(self):
        return self.initial["password"]