# Generated by Django 2.2.3 on 2019-07-31 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_booking_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='child',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='total_rooms',
        ),
    ]