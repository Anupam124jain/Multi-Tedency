# Generated by Django 2.1.4 on 2018-12-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tenant',
            old_name='is_verified',
            new_name='is_active',
        ),
        migrations.AlterField(
            model_name='tenant',
            name='industry',
            field=models.CharField(choices=[('ICO', 'ICO'), ('FinancialService', 'FinancialService'), ('Others', 'Others'), ('1', ' '), ('HealthCare ', 'HealthCare')], default='1', max_length=50),
        ),
        migrations.AlterField(
            model_name='tenant',
            name='role',
            field=models.CharField(choices=[('Product', 'Product'), ('Marketing', 'Marketing'), ('Others', 'Others'), ('1', ' '), ('Risk ', 'Risk'), ('Innvation', 'Innvation')], default='1', max_length=50),
        ),
    ]
