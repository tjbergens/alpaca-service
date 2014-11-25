from rest_framework import serializers
from purplealpaca.models import Account
from django.contrib.auth.models import User


class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')

    class Meta:
        model = Account
        fields = ('id', 'accountName', 'userName', 'password')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')

class UserDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        write_only_fields = ('password',)
