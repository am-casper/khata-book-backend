from rest_framework import serializers

from transactions.models import Transactions


class TransactionSerializer(serializers.ModelSerializer):
    transaction_date = serializers.DateField(required=False)
    transaction_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    credit_user = serializers.CharField(max_length=10)
    debit_user = serializers.CharField(max_length=10)
    
    class Meta:
        model = Transactions
        fields = ('transaction_date', 'transaction_amount', 'credit_user', 'debit_user')