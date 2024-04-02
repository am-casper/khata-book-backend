# Generated by Django 5.0.3 on 2024-04-02 12:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("user", "0004_alter_user_phone"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transactions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("transaction_date", models.DateTimeField()),
                (
                    "transaction_amount",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "credit_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user",
                        to="user.user",
                    ),
                ),
            ],
        ),
    ]