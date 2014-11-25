from rest_framework import serializers
from purplealpaca.models import Account
from django.contrib.auth.models import User

# Serializer used to turn JSON requests into Python datatypes
class AccountSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')

    class Meta:
        model = Account
        fields = ('id', 'accountName', 'userName', 'password')

# Serializer used to turn Main User account JSON requests into Python datatypes
class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
# Serializer used to turn Main User account authentication requests into Python datatypes
class UserAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password')

# Serializer used to turn Main User account destruction requests into Python datatypes
class UserDelSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        write_only_fields = ('password',)
