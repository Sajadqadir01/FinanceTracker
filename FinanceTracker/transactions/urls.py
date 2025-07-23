from . import views
from django.urls import path
urlpatterns =[
    path('', views.home, name='home'),
    path('transaction', views.TransactionView.as_view(), name='transaction'),
    path('add_account', views.AccountView.as_view(), name='add_account'),
    path('add_category', views.CategoryView.as_view(), name='add_category')
]