# Generated by Django 4.1.7 on 2023-03-09 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0008_order_paid_order_payment_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='additional_info',
        ),
    ]
