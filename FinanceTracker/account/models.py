from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UserManager(BaseUserManager):
    def create_user(self, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError("شماره تماس الزامیست")
        phone = self.normalize_email(phone)
        extra_fields.setdefault('is_active', True)
        user = self.model(phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if not extra_fields.get('is_staff'):
            raise ValueError("کاربر ادمین باید دسترسی مدیریت داشته باشد (is_staff=True)")
        if not extra_fields.get('is_superuser'):
            raise ValueError("کاربر ادمین باید دسترسی سوپر یوزر داشته باشد (is_superuser=True)")

        return self.create_user(phone, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('ایمیل'), unique=True, null=True, blank=True)
    first_name = models.CharField(_('نام'), max_length=150, blank=True)
    last_name = models.CharField(_('نام خانوادگی'), max_length=150, blank=True)
    phone = models.CharField(_('شماره تماس'), max_length=20, blank=True, unique=True)
    is_staff = models.BooleanField(_('کارمند'), default=False)
    is_active = models.BooleanField(_('فعال'), default=True)
    date_joined = models.DateTimeField(_('تاریخ عضویت'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'email']

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.email
