# Generated by Django 4.0.5 on 2022-07-01 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_organization_fraud_weight_bill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='date',
            field=models.DateField(),
        ),
    ]