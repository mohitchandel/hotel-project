# Generated by Django 2.2.3 on 2019-07-29 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0013_auto_20190729_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='arv_date',
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='booking',
            name='child',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='cust_name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='booking',
            name='dep_dte',
            field=models.CharField(default=None, max_length=25),
        ),
        migrations.AlterField(
            model_name='booking',
            name='persons',
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room_type',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
