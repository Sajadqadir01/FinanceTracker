from django import forms
from . import models

class CreateTransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        exclude = ['user']
        widgets ={
            'amount': forms.NumberInput(attrs={
                'class': 'form-control text-end',
                'placeholder': 'مثلاً ۵۰۰۰۰۰',
                'style': 'border-radius:10px; background:#f5f5f5; color:#111; border:1px solid #ccc;',
            }),

            'transaction_type': forms.Select(attrs={
                'class': 'form-select text-center',
                'style': 'border-radius:10px; background:#f5f5f5; border:1px solid #ccc;',
            }),

            'category': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-radius:10px; background:#f5f5f5; border:1px solid #ccc;',
            }),

            'account': forms.Select(attrs={
                'class': 'form-select',
                'style': 'border-radius:10px; background:#f5f5f5; border:1px solid #ccc;',
            }),

            'description': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'توضیحات تراکنش (اختیاری)',
                'class': 'form-control',
                'style': 'border-radius:10px; background:#f5f5f5; border:1px solid #ccc;',
            }),

            'date': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'style': 'border-radius:10px; background:#f5f5f5; border:1px solid #ccc;',
            }),

            'receipt': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'style': 'border-radius:10px; background:#fff; border:1px solid #ccc;',
            }),

            'is_confirmed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'style': 'transform: scale(1.2); margin-right:10px;',
            }),
        }
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user:
            self.fields['category'].queryset = models.Category.objects.filter(user=user)
            self.fields['account'].queryset = models.Account.objects.filter(user=user)
            



class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = models.Account
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)




class CreateCategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = '__all__'
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
