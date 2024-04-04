from django.urls import path
from . import views

urlpatterns = [
    path('', views.TransactionsDetailView.as_view(), name='transaction-detail'),
    path('create', views.TransactionCreateView.as_view(), name='transaction-create'),
]