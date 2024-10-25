from django.urls import path
from .views import PaymentAccountsApi, AllTransactionApi, PaymentAccountApi

urlpatterns = [
    path("all_accounts", PaymentAccountsApi.as_view()),
    path("all_accounts/", PaymentAccountsApi.as_view()),
    path("account/<int:id>", PaymentAccountApi.as_view()),
    path("all_transactions/", AllTransactionApi.as_view()),
    path("all_transactions", AllTransactionApi.as_view()),
    path("transaction/", AllTransactionApi.as_view()),
]