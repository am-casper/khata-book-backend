from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from transactions.models import Transactions
from transactions.serializer import TransactionSerializer
from user.models import User
from django.db.models import Q

from datetime import date


class TransactionCreateView(APIView):
    def post(self, request):
        serializer = TransactionSerializer(data=request.data)
        if serializer.is_valid():
            t_date= serializer.validated_data.get('transaction_date')
            if(t_date== None ):
                t_date=date.today()
            credit_user=User.objects.filter(phone=serializer.validated_data.get('credit_user'))[0]
            debit_user=User.objects.filter(phone=serializer.validated_data.get('debit_user'))[0]
            transaction = Transactions.objects.create(
                transaction_date=t_date, 
                transaction_amount=serializer.validated_data.get( 'transaction_amount'), 
                credit_user=credit_user, 
                debit_user=debit_user)
            credit_user.balance += transaction.transaction_amount
            debit_user.balance -= transaction.transaction_amount
            credit_user.save()
            debit_user.save()
            transaction.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class TransactionsDetailView(APIView):
    def get(self, request):
        cr = Transactions.objects.filter(credit_user=User.objects.filter(phone=request.query_params.get('phone'))[0])
        dr = Transactions.objects.filter(debit_user=User.objects.filter(phone=request.query_params.get('phone'))[0])
        dr_list = [None]*len(dr)
        cr_list = [None]*len(cr)
        for i in range(len(dr)):
            transaction = dr[i]
            tran = {
                'transaction_date': transaction.transaction_date,
                'transaction_amount': -transaction.transaction_amount,
                'user': transaction.credit_user.name
            }
            dr_list[i] = tran
        for i in range(len(cr)):
            transaction = cr[i]
            tran = {
                'transaction_date': transaction.transaction_date,
                'transaction_amount': transaction.transaction_amount,
                'user': transaction.debit_user.name
            }
            cr_list[i] = tran
        transactions = cr_list + dr_list
        sorted_transactions = sorted(transactions, key=lambda transaction: transaction['transaction_date'], reverse=True) 
        return Response(sorted_transactions, status=200)
    
