from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from .models import PaymentAccountModel, TransactionModel
from .serializers import PaymentAccountSerializer, TransactionSerializer


class PaymentAccountsApi(APIView):
    """Get All Payment Accounts and POST new PaymentAccounts"""
    serializer_class = PaymentAccountSerializer
    model = PaymentAccountModel

    def get(self, request):
        queryset = PaymentAccountModel.objects.all()
        serializer_for_queryset = PaymentAccountSerializer(instance=queryset, many=True)
        return Response(serializer_for_queryset.data)

    def post(self, request):
        acc = PaymentAccountModel()
        acc.currency = request.data["currency"]
        acc.save()
        return Response(request.data, status=status.HTTP_201_CREATED)

class PaymentAccountApi(APIView):
    """Get Payment Account by ID and POST new PaymentAccounts"""
    serializer_class = PaymentAccountSerializer
    model = PaymentAccountModel

    def get(self, request, id):
        queryset = PaymentAccountModel.objects.get(pk=id)
        print(PaymentAccountModel.objects.get(pk=id).get_from_transactions_list)
        serializer_for_queryset = PaymentAccountSerializer(instance=[queryset], many=True)
        return Response(serializer_for_queryset.data)

    def post(self, request):
        acc = PaymentAccountModel()
        acc.currency = request.data["currency"]
        acc.save()
        return Response(request.data, status=status.HTTP_201_CREATED)


class AllTransactionApi(APIView):
    serializer_class = TransactionSerializer
    model = TransactionModel

    def get(self, request):
        queryset = TransactionModel.objects.all()
        serializer_for_queryset = TransactionSerializer(instance=queryset, many=True)
        return Response(serializer_for_queryset.data)

    def post(self, request):
        print(request.data["from_acc"])
        transaction = TransactionModel()
        transaction.from_acc = PaymentAccountModel.objects.get(pk=request.data["from_acc"])
        transaction.to_acc = PaymentAccountModel.objects.get(pk=request.data["to_acc"])
        transaction.sum = request.data["sum"]
        transaction.save()
        return Response(request.data, status=status.HTTP_201_CREATED)