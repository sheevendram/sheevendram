# Generated by Django 4.0 on 2022-08-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceitem',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='amount_paid',
            field=models.IntegerField(default=0),
        ),
    ]