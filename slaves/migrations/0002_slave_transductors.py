# Generated by Django 2.1.5 on 2019-10-16 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transductors', '0002_auto_20190930_0943'),
        ('slaves', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slave',
            name='transductors',
            field=models.ManyToManyField(related_name='slave_servers', to='transductors.EnergyTransductor'),
        ),
    ]
