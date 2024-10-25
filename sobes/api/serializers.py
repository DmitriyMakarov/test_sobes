from rest_framework import serializers
from .models import PaymentAccountModel, TransactionModel


class PaymentAccountSerializer(serializers.ModelSerializer):
    balance_field = serializers.ReadOnlyField(source="balance")
    outgoing_field = serializers.ReadOnlyField(source="get_from_transactions_list")
    incoming_field = serializers.ReadOnlyField(source="get_in_transactions_list")

    class Meta:
        model = PaymentAccountModel
        fields = "__all__"
        depth = 1


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransactionModel
        fields = "__all__"