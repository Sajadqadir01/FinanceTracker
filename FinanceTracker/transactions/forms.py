from django import forms
from . import models

class CreateTransactionForm(forms.ModelForm):
    class Meta:
        model = models.Transaction
        exclude = ['user']

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
