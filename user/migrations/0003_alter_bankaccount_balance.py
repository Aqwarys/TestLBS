# Generated by Django 5.1.6 on 2025-03-06 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_bankaccount_balance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='balance',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
