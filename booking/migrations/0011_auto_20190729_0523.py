# Generated by Django 2.2.3 on 2019-07-29 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0010_remove_booking_rooms_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='rooms',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room_type',
            field=models.CharField(default='', max_length=20),
        ),
    ]