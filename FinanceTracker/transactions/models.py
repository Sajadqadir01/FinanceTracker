from django.db import models
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    ACCOUNT_TYPES = (
        ('cash', 'نقدی'),
        ('card', 'کارت بانکی'),
    )
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, verbose_name="کاربر")
    name = models.CharField(max_length=100, verbose_name="نام حساب")
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES, verbose_name="نوع حساب")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "حساب مالی"
        verbose_name_plural = "حساب‌های مالی"

    def __str__(self):
        return f"{self.name} ({self.get_account_type_display()})"


class Category(models.Model):
    CATEGORY_TYPES = (
        ('income', 'درآمد'),
        ('expense', 'هزینه'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, verbose_name="کاربر")
    name = models.CharField(max_length=100, verbose_name="نام دسته‌بندی")
    type = models.CharField(max_length=10, choices=CATEGORY_TYPES, verbose_name="نوع")

    class Meta:
        verbose_name = "دسته‌بندی"
        verbose_name_plural = "دسته‌بندی‌ها"

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'درآمد'),
        ('expense', 'هزینه'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, editable=False, verbose_name="کاربر")
    amount = models.IntegerField(verbose_name="مبلغ")
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES, verbose_name="نوع تراکنش")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="دسته‌بندی")
    account = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="حساب مالی")
    description = models.TextField(blank=True, verbose_name="توضیحات")
    date = models.DateTimeField(verbose_name="تاریخ تراکنش")
    receipt = models.ImageField(upload_to='receipts/', null=True, blank=True, verbose_name="تصویر رسید (اختیاری)")
    is_confirmed = models.BooleanField(default=False, verbose_name="تأیید شده؟")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="ایجاد در")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="به‌روزرسانی در")

    class Meta:
        verbose_name = "تراکنش"
        verbose_name_plural = "تراکنش‌ها"

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} در {self.date.date()}"
