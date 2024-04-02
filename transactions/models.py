from django.db import models

from user.models import User

class Transactions(models.Model):
    transaction_date = models.DateField()
    transaction_amount = models.DecimalField(max_digits=10, decimal_places=2)
    credit_user = models.ForeignKey(User,related_name="user1", on_delete=models.CASCADE)
    debit_user = models.ForeignKey(User,related_name="user2", on_delete=models.CASCADE)
