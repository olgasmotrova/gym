from django.contrib import admin

from datagym.models import Gym, Address, Subscription, Client


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('city', 'street', 'apartment', 'phone')
    list_filter = ('city', 'street', 'apartment', 'phone')
    ordering = ['phone']


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('name', 'per_num', 'status', 'is_activated', 'due_date')
    list_filter = ('name', 'per_num', 'status', 'is_activated', 'due_date')
    ordering = ['due_date']


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'birth_date', 'registration_date', 'subscription_num')
    list_filter = ('first_name', 'last_name', 'phone', 'birth_date', 'registration_date', 'subscription_num')
    ordering = ['subscription_num']


@admin.register(Gym)
class GymAdmin(admin.ModelAdmin):
    list_display = ('address', 'status')
    list_filter = ('address', 'status', 'clients')
    ordering = ['address']


