# Generated by Django 5.0.3 on 2024-04-02 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transactions", "0003_remove_transactions_credit_user_and_more"),
        ("user", "0005_alter_user_phone"),
    ]

    operations = [
        migrations.DeleteModel(
            name="User",
        ),
    ]
