from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import logout, login, authenticate
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import User
from app_apartment.models import Address, Apartment
from app_chat.models import Message


def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except ValidationError:
        return False


def is_valid_phone(phone):
    if phone[1:].isdigit():
        if phone.startswith('+989') and len(phone) == 13:
            return True
        if phone.startswith('9') and len(phone) == 10:
            return True
        if phone.startswith('0') and len(phone) == 11:
            return True
    return False


class Login(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse_lazy('home'))
        else:
            return render(request, 'login.html', {
                'message': 'not_found',
                'email': email
            })


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password1')
        password_again = request.POST.get('password2')

        error = None
        if not is_valid_email(email):
            error = 'not_valid_email'
        elif User.objects.filter(email=email).exists():
            error = 'duplicate_email'
        elif password != password_again:
            error = 'not_same_password'
        elif not is_valid_phone(phone):
            error = 'not_valid_phone'

        if error is not None:
            return render(request, 'register.html', {
                'message': error,
                'first_name': firstname,
                'last_name': lastname,
                'email': email,
                'phone': phone
            })
        else:
            User.objects.create_user(
                first_name=firstname,
                last_name=lastname,
                email=email,
                phone=phone,
                password=password
            )
            return render(request, 'login.html', {'message': 'success_register'})


class Logout(View):
    def get(self, request):
        if request.user.is_authenticated:
            logout(request)
        return redirect(reverse_lazy('home'))


class Dashboard(LoginRequiredMixin, View):
    def get(self, request):
        locations = sorted(Address.objects.all().values_list('name', flat=True))
        home_count = len(Apartment.objects.filter(person=request.user))
        message_count = len(Message.objects.filter(Q(sender=request.user) | Q(recipient=request.user)))
        return render(request, 'dashboard.html', {
            'locations': locations,
            'home_count': home_count,
            'message_count': message_count
        })
