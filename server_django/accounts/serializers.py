from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
  class Meta:
    model = Account
    fields = '__all__'
    # fields = ['email', 'given_name', 'name', 'is_admin']
