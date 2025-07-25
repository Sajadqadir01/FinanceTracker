# Generated by Django 5.2.4 on 2025-07-20 20:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام حساب')),
                ('account_type', models.CharField(choices=[('cash', 'نقدی'), ('card', 'کارت بانکی')], max_length=10, verbose_name='نوع حساب')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'حساب مالی',
                'verbose_name_plural': 'حساب\u200cهای مالی',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='نام دسته\u200cبندی')),
                ('type', models.CharField(choices=[('income', 'درآمد'), ('expense', 'هزینه')], max_length=10, verbose_name='نوع')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'دسته\u200cبندی',
                'verbose_name_plural': 'دسته\u200cبندی\u200cها',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='مبلغ')),
                ('transaction_type', models.CharField(choices=[('income', 'درآمد'), ('expense', 'هزینه')], max_length=10, verbose_name='نوع تراکنش')),
                ('description', models.TextField(blank=True, verbose_name='توضیحات')),
                ('date', models.DateTimeField(verbose_name='تاریخ تراکنش')),
                ('receipt', models.ImageField(blank=True, null=True, upload_to='receipts/', verbose_name='تصویر رسید (اختیاری)')),
                ('is_confirmed', models.BooleanField(default=False, verbose_name='تأیید شده؟')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='ایجاد در')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='به\u200cروزرسانی در')),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transactions.account', verbose_name='حساب مالی')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='transactions.category', verbose_name='دسته\u200cبندی')),
                ('user', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'تراکنش',
                'verbose_name_plural': 'تراکنش\u200cها',
            },
        ),
    ]
