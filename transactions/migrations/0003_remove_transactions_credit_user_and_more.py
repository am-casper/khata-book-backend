# Generated by Django 5.0.3 on 2024-04-02 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0002_transactions_debit_user_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="transactions",
            name="credit_user",
        ),
        migrations.RemoveField(
            model_name="transactions",
            name="debit_user",
        ),
    ]
