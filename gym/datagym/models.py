from datetime import date

from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Address(models.Model):
    city = models.CharField(max_length=225, blank=False)
    street = models.CharField(max_length=225, blank=False)
    apartment = models.CharField(max_length=4, blank=False)
    phone = models.CharField(verbose_name='Contact us:', max_length=13,
                             default='+380000000000', blank=False)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return f"{self.city}, {self.street} {self.apartment}"


class Subscription(models.Model):
    #TODO счетчик посещений

    ROLE = [
        ('30', '30'),
        ('8', '8'),
        ('12', '12')
    ]
    TYPE = [
        ('individual', 'Individual'),
        ('group', 'Group'),
        ('independent', 'Independent')
    ]
    name = models.CharField(max_length=20, choices=TYPE, default='independent')
    per_num = models.CharField(verbose_name='Personal number', max_length=7, default=0000000, blank=False)
    status = models.CharField(max_length=2, choices=ROLE, default='30')
    is_activated = models.BooleanField(verbose_name='Active', default=False)
    due_date = models.DateField(verbose_name='Expires', default=timezone.now, null=True, blank=True)

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    def __str__(self):
        return f'№ {self.per_num}'


class Client(models.Model):
    first_name = models.CharField(max_length=100, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    phone = models.CharField(verbose_name='Contact:', max_length=12,
                             default='+380000000000', blank=False, unique=True)
    subscription_num = models.ForeignKey(Subscription, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=False)
    registration_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        return self.last_name


class Gym(models.Model):
    #TODO график работы
    #TODO сделать выпадающий список (если адрес один, то зал один и телефон общий!
    # Если у зала много клиентов, то выпадающий список клиентов)
    STATUS = [
        ('open', 'Open'),
        ('closed', 'Closed')
    ]
    address = models.ForeignKey(Address, blank=False, on_delete=models.CASCADE)
    clients = models.ManyToManyField(Client)
    status = models.CharField(max_length=10, choices=STATUS, default='open')

    class Meta:
        verbose_name = 'Gym'
        verbose_name_plural = 'Gyms'

    def __str__(self):
        return str(self.address)


