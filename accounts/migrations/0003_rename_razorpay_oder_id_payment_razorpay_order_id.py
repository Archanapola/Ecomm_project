# Generated by Django 4.1.2 on 2024-10-26 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_payment_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='razorpay_oder_id',
            new_name='razorpay_order_id',
        ),
    ]
