# Generated by Django 2.2.3 on 2019-07-29 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0015_auto_20190729_0559'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='phone_num',
            field=models.CharField(default=None, max_length=40),
        ),
    ]
