from django.contrib import admin
from .models import Account, Category, Transaction

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'account_type', 'user', 'created_at')
    search_fields = ('name', 'user__username')
    list_filter = ('account_type',)
    def save_model(self, request, obj, form, change):
        if not obj.user_id:  # فقط اگه کاربر هنوز تنظیم نشده
            obj.user = request.user
        obj.save()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')
    list_filter = ('type',)
    search_fields = ('name',)
    def save_model(self, request, obj, form, change):
        if not obj.user_id:  # فقط اگه کاربر هنوز تنظیم نشده
            obj.user = request.user
        obj.save()


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'transaction_type', 'category', 'account', 'is_confirmed', 'date')
    list_filter = ('transaction_type', 'is_confirmed', 'date')
    search_fields = ('description',)
    date_hierarchy = 'date'
    def save_model(self, request, obj, form, change):
        if not obj.user_id:  # فقط اگه کاربر هنوز تنظیم نشده
            obj.user = request.user
        obj.save()
    