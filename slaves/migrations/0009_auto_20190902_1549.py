# Generated by Django 2.1.5 on 2019-09-02 18:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slaves', '0008_merge_20190902_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slave',
            name='ip_address',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator('^(?:[0-9]{1,3}\\.){3}[0-9]{1,3}$', 'Incorrect IP address format')]),
        ),
    ]
