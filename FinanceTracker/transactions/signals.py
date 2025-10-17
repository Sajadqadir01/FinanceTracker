from django.db.models.signals import post_save, pre_save, post_delete
from django.dispatch import receiver
from .models import Transaction


@receiver(pre_save, sender=Transaction)
def adjust_balance_on_update(sender, instance, **kwargs):
    if not instance.pk:
        return  

    try:
        old_transaction = Transaction.objects.get(pk=instance.pk)
    except Transaction.DoesNotExist:
        return

    user = instance.user


    if old_transaction.transaction_type == 'income':
        user.balance -= old_transaction.amount
    elif old_transaction.transaction_type == 'expense':
        user.balance += old_transaction.amount

    user.save()


@receiver(post_save, sender=Transaction)
def update_balance_on_create_or_edit(sender, instance, created, **kwargs):
    user = instance.user

    if instance.transaction_type == 'income':
        user.balance += instance.amount
    elif instance.transaction_type == 'expense':
        user.balance -= instance.amount

    user.save()


@receiver(post_delete, sender=Transaction)
def update_balance_on_delete(sender, instance, **kwargs):
    user = instance.user

    if instance.transaction_type == 'income':
        user.balance -= instance.amount
    elif instance.transaction_type == 'expense':
        user.balance += instance.amount

    user.save()