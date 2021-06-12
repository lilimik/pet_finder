from django.contrib.auth.models import AbstractUser
from django.db import models
from djchoices import DjangoChoices, ChoiceItem

from users.managers import CustomUserManager


class Role(DjangoChoices):
    admin = ChoiceItem()
    user = ChoiceItem()


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    patronymic = models.CharField(max_length=150, verbose_name='Отчество', null=True, blank=True)
    avatar = models.ImageField(upload_to='user_avatars', verbose_name='аватар', null=False, blank=False)
    age = models.PositiveSmallIntegerField(verbose_name='возраст', null=True, blank=True)
    birthday = models.DateTimeField(verbose_name='День рождения', null=True, blank=True)
    phone_number = models.CharField(max_length=11, verbose_name='номер телефона', null=False, blank=False)
    role = models.CharField(max_length=50, choices=Role.choices, default=Role.user)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email} - {self.phone_number} - {self.role}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class PetCategory(DjangoChoices):
    cat = ChoiceItem()
    dog = ChoiceItem()


class Pet(models.Model):
    owner = models.ManyToManyField(CustomUser, verbose_name='владелец')
    category = models.CharField(max_length=50, choices=PetCategory.choices, verbose_name='категория', null=False,
                                blank=False)
    age = models.PositiveSmallIntegerField(verbose_name='возраст', null=True, blank=True)
    name = models.CharField(max_length=150, verbose_name='имя', null=False, blank=False)
    breed = models.CharField(max_length=250, verbose_name='порода', null=True, blank=True)
    avatar = models.ImageField(upload_to='animal_avatars', verbose_name='аватар', null=False, blank=False)
    lost_status = models.BooleanField(verbose_name='статус пропажи', default=False, null=False, blank=False)
    short_link = models.URLField(verbose_name='короткая ссылка', null=False, blank=False)

    def __str__(self):
        return f'{self.name} - lost status: {self.lost_status} - {self.short_link}'

    class Meta:
        verbose_name = 'Питомец'
        verbose_name_plural = 'Питомцы'


class FinderFormsModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='находчик', related_name='forms',
                             null=False, blank=False)
    photo = models.ImageField(upload_to='finder_forms_photos', verbose_name='фото', null=True, blank=True)
    phone_number = models.CharField(max_length=11, verbose_name='номер телефона', null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    lat = models.CharField(max_length=100, verbose_name='широта', null=True, blank=True)
    lot = models.CharField(max_length=100, verbose_name='долгота', null=True, blank=True)
