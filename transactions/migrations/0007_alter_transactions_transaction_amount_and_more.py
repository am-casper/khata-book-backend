# Generated by Django 5.0.3 on 2024-04-04 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0006_alter_transactions_transaction_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="transactions",
            name="transaction_amount",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name="transactions",
            name="transaction_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
