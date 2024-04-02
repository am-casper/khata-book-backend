# Generated by Django 5.0.3 on 2024-04-02 13:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0003_remove_transactions_credit_user_and_more"),
        ("user", "0007_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="transactions",
            name="credit_user",
            field=models.ForeignKey(
                default="123",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user1",
                to="user.user",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="transactions",
            name="debit_user",
            field=models.ForeignKey(
                default="123",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user2",
                to="user.user",
            ),
            preserve_default=False,
        ),
    ]