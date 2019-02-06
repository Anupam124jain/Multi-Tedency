# Generated by Django 2.1.4 on 2018-12-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0006_auto_20181214_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tenant',
            name='industry',
            field=models.CharField(choices=[(1, ' '), ('Others', 'Others'), ('ICO', 'ICO'), ('FinancialService', 'FinancialService'), ('HealthCare', 'HealthCare')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='role',
            field=models.CharField(choices=[(1, ' '), ('Marketing', 'Marketing'), ('Product', 'Product'), ('Others', 'Others'), ('Risk', 'Risk'), ('Innvation', 'Innvation')], default=1, max_length=50),
        ),
    ]
