from django.urls import path
from . import views
urlpatterns =[
    path('register', views.RegisterView.as_view(), name='register'),
    path('login', views.CustomLoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.UserDashboardView.as_view(), name='dashboard'),
    path('account-info/', views.AccountInfoView.as_view(), name='account_info'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    path('initial-asset/', views.InitialAssetView.as_view(), name='initial_asset'),
]