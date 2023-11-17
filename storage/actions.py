from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

from storage.models import Client


def auth(request):
    """ Авторизация пользователя

    До авторизации request.user="AnonymousUser"
    После авторизации request.user=user(email)
    """
    username = request.POST['EMAIL']
    password = request.POST['PASSWORD']
    try:
        user = authenticate(username=username, password=password)
    except:
        user=None
    if not user:
        request.session['message'] = 'Ошибка авторизации'
        return 0
    login(request, user)
    user = User.objects.get(username=username)
    request.session['user_name'] = user.first_name
    return 0


def registration(request):
    """Регистрация

    Сохраняем имя в first_name объекта user,
    почту используем в качестве логина
    Проверяем подтвержение пароля и уникальность логина (почты)
    """

    first_name = request.POST['NAME_CREATE']
    username = request.POST['EMAIL_CREATE']
    email = request.POST['EMAIL_CREATE']
    password = request.POST['PASSWORD_CREATE']
    passwordconfirm = request.POST['PASSWORD_CONFIRM']

    if password != passwordconfirm:
        request.session['message'] = 'Пароли не совпадают'
        return 0

    try:
        user = User.objects.create_user(
            first_name=first_name,
            username=username,
            password=password,
            email=email,
        )
        client = Client.objects.create(
            user=user,
        )
    except:
        request.session['message'] =  'Пользователь с такой почтой существует'
        return 0
    login(request, user)
    request.session['user_name'] = first_name
    return 0


def deauth(request):
    logout(request)
    request.session['user_name'] = ''
    return redirect('/')


def send_message(*args):
    """
    Здесь будет код
    """
    return redirect('admin/storage/order')

def send_check(*args):
    """
    Здесь будет код
    """
    return redirect('admin/storage/order')

def create_client(*args):
    """
    Здесь будет код
    """
    return redirect('admin/storage/client')

def send_message(*args):
    """
    Здесь будет код
    """
    return redirect('admin/storage/client')