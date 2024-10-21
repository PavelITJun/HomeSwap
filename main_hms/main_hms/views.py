from django.shortcuts import get_object_or_404, render, redirect
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.views import View
from django.contrib.auth.decorators import login_required
from .serializers import RegistrationSerializer
import logging
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse_lazy
from .forms import SetPasswordForm


User = get_user_model()

logger = logging.getLogger(__name__)


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'main_hms/password_reset_confirm.html'
    success_url = reverse_lazy('password-reset-complete')
    form_class = SetPasswordForm


def index(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    context = {'user': user, 'title': 'Main page'}
    return render (request, 'main_hms/index.html', context)


def about(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    context = {'user': user, 'title': 'How it works'}
    return render (request, 'main_hms/about.html', context)


class UserRegistrationView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def get(self, request, *args, **kwargs):
        return render(request, 'main_hms/register.html', {'title': 'Регистрация'})

    def post(self, request, *args, **kwargs):
        logger.info("Полученные данные: %s", request.data)  # Логируем данные
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Сохраняем пользователя
            logger.info("Пользователь успешно сохранён: %s", user)  # Логируем успешное сохранение
            return redirect('registration_success')
        
        logger.warning("Ошибки валидации: %s", serializer.errors)  # Логируем ошибки
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def registration_success(request):
    return render(request, 'main_hms/success_reg.html', {'title': 'Регистрация прошла успешно'})


class LoginView(View):
    def get(self, request):
        return render(request, 'main_hms/login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        logger.info("Попытка входа с email: %s", email)

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            logger.info("Пользователь вошел: %s", user.email)
            return redirect('auth_success')
        else:
            logger.warning("Неверные учетные данные для email: %s", email)
            error = 'Неправильный email или пароль.'
            return render(request, 'main_hms/login.html', {'error': error})
        

def auth_success(request):
    return render(request, 'main_hms/success_auth.html', {'title': 'Авторизация прошла успешно'})


def access_denied(request):
    return render(request, 'main_hms/access_denied.html')


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

        
@login_required
def auth_test(request):
    return Response({'message': 'Ты авторизован!'})