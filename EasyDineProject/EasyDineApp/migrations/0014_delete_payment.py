# Generated by Django 4.2.13 on 2024-05-16 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EasyDineApp', '0013_alter_payment_invoice_number'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
