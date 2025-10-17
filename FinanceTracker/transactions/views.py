from django.contrib import messages
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import CreateTransactionForm, CreateAccountForm, CreateCategoryForm
from .models import Transaction, Account, Category
from django.contrib.auth import get_user_model

User = get_user_model()

def home(request):
    return render(request, 'transactions/home.html')

class TransactionView(LoginRequiredMixin, FormView):
    model = Transaction
    template_name = 'transactions/createtransaction.html'
    form_class = CreateTransactionForm
    success_url = reverse_lazy('transaction')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        user = self.request.user
        transaction = form.save(commit=False)

        user.save()
        transaction.user = user
        transaction.save()

        messages.success(self.request, "تراکنش با موفقیت ثبت شد.")
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class AccountView(LoginRequiredMixin, FormView):
    model = Account
    template_name = 'transactions/quick_add_account.html'
    form_class = CreateAccountForm
    success_url = reverse_lazy('transaction')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        account = form.save(commit=False)
        account.user = self.request.user
        account.save()
        return super().form_valid(form)


class CategoryView(LoginRequiredMixin, FormView):
    model = Category
    template_name = 'transactions/quick_add_category.html'
    form_class = CreateCategoryForm
    success_url = reverse_lazy('transaction')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        category = form.save(commit=False)
        category.user = self.request.user
        category.save()
        return super().form_valid(form)