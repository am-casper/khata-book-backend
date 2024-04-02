# Generated by Django 5.0.3 on 2024-04-02 11:19

import phonenumber_field.modelfields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_remove_user_id_alter_user_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="phone",
            field=phonenumber_field.modelfields.PhoneNumberField(
                max_length=128, primary_key=True, region=None, serialize=False
            ),
        ),
    ]