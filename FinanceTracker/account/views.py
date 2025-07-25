from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import FormView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from .forms import LoginForm, RegisterForm, InitialBalance, UpdateUserForm, CustomPasswordChangeForm
from django.views.generic import TemplateView

from .models import CustomUser


class CustomLoginView(LoginView):
    template_name = 'account/login.html'
    authentication_form = LoginForm
    redirect_authenticated_user = True


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')


class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password1'])
        user.save()
        login(self.request, user)
        return super().form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return super().dispatch(request, *args, **kwargs)


class InitialAssetView(LoginRequiredMixin, FormView):
    template_name = 'account/initial_asset.html'
    form_class = InitialBalance
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        amount = form.cleaned_data['amount']
        user = self.request.user
        user.balance = amount
        user.save()
        return super().form_valid(form)


class UserDashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'account/dashboard.html'

class AccountInfoView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UpdateUserForm
    template_name = 'account/account_info.html'
    success_url = reverse_lazy('dashboard')

    def get_object(self):
        return self.request.user


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'account/change_password.html'
    form_class = CustomPasswordChangeForm
    success_url = reverse_lazy('login')
