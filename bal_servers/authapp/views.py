from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, UpdateView, DetailView
from .forms import CustomUserCreationForm, CustomUserAuthenticationForm, CustomUserChangeForm


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = 'authapp/login.html'
    authentication_form = CustomUserAuthenticationForm
    success_message = 'Авторизация прошла успешно.'
    extra_context = {'title': 'Вход'}

    def get_success_url(self):
        """
        Почему то проходит только такой редирект
        """
        return reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, 'Неверно указаны логин или пароль')
        return super().form_invalid(form)


class RegisterView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('authapp:login')
    template_name = 'authapp/register.html'
    success_message = 'Аккаунт зарегистрирован.'
    extra_context = {'title': 'Регистрация'}


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')


class CustomUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'authapp/edit.html'
    form_class = CustomUserChangeForm
    success_url = '/auth/profile'
    success_message = 'Профиль успешно обновлен.'
    extra_context = {'title': 'Профиль'}

    def get_object(self, queryset=None):
        return self.request.user


class UserProfileView(DetailView):
    model = get_user_model()
    template_name = 'authapp/profile.html'
    context_object_name = 'user_profile'

    def get_object(self, queryset=None):
        return self.request.user