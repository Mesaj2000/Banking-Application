# Generated by Django 3.1.1 on 2020-11-03 00:29

from django.db import migrations, models
import view_balances.models


class Migration(migrations.Migration):

    dependencies = [
        ('view_balances', '0002_auto_20201103_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='account_type',
            field=models.CharField(choices=[(view_balances.models.Account_Type['CHECKING'], 'Checking'), (view_balances.models.Account_Type['SAVINGS'], 'Savings')], default='Checking', max_length=10),
            preserve_default=False,
        ),
    ]