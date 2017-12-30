from rest_framework import serializers

from base.accounting.models import Bank


class BankSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bank
        fields = '__all__'