# Generated by Django 2.2.3 on 2019-07-29 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0014_auto_20190729_0535'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='rooms_total',
            new_name='total_rooms',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='arv_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='cust_name',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='dep_dte',
        ),
        migrations.AddField(
            model_name='booking',
            name='arval_date',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='booking',
            name='customer_name',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AddField(
            model_name='booking',
            name='dep_date',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AlterField(
            model_name='booking',
            name='child',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AlterField(
            model_name='booking',
            name='persons',
            field=models.CharField(default=None, max_length=40),
        ),
        migrations.AlterField(
            model_name='booking',
            name='room_type',
            field=models.CharField(default=None, max_length=40),
        ),
    ]
