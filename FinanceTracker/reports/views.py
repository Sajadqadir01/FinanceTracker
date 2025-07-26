from django.shortcuts import render
from django.views.generic.dates import DateMixin
from transactions.models import Transaction
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum


class DashboardView(ListView, LoginRequiredMixin, DateMixin):
    model = Transaction
    date_field = 'date'
    template_name = 'reports/report_dashboard.html'
    paginate_by = 1

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        transactions = self.get_queryset()
        recent_transactions = Transaction.objects.filter(user=user).order_by('-created_at')[:5]

        income_total = transactions.filter(transaction_type='income').aggregate(total=Sum('amount'))['total'] or 0
        expense_total = transactions.filter(transaction_type='expense').aggregate(total=Sum('amount'))['total'] or 0

        # جمع درآمد و هزینه به تفکیک ماه برای نمودار
        monthly_income = {}
        monthly_expense = {}
        for t in transactions:
            month = t.date.strftime('%Y-%m')
            if t.transaction_type == 'income':
                monthly_income[month] = monthly_income.get(month, 0) + t.amount
            elif t.transaction_type == 'expense':
                monthly_expense[month] = monthly_expense.get(month, 0) + t.amount

        all_months = sorted(set(monthly_income.keys()) | set(monthly_expense.keys()))

        context.update({
            'income_total': income_total,
            'expense_total': expense_total,
            'balance': user.balance,
            'transaction_count': transactions.count(),
            'transactions': recent_transactions,
            'labels': all_months,
            'income_data': [monthly_income.get(m, 0) for m in all_months],
            'expense_data': [monthly_expense.get(m, 0) for m in all_months],
        })
        return context