from rest_framework import serializers

from datagym.models import Gym, Client, Address, Subscription


class GymSerializer(serializers.ModelSerializer):

    class Meta:
        model = Gym
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'


