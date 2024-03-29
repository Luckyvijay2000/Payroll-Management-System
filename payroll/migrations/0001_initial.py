# Generated by Django 3.0 on 2023-06-25 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('employee_id', models.CharField(max_length=10, unique=True)),
                ('designation', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=250)),
                ('PAN', models.CharField(max_length=120)),
                ('Account_number', models.CharField(max_length=20)),
                ('basic', models.FloatField()),
                ('AGP', models.FloatField()),
                ('Pay', models.FloatField()),
                ('PP', models.FloatField()),
                ('DA', models.FloatField()),
                ('HRA', models.FloatField()),
                ('Others', models.FloatField()),
                ('GPF', models.FloatField()),
                ('GIS', models.FloatField()),
                ('CPS', models.FloatField()),
                ('PT', models.FloatField()),
                ('IT', models.FloatField()),
                ('LIC1', models.FloatField()),
                ('LIC2', models.FloatField()),
                ('HR', models.FloatField()),
                ('V_ADV', models.FloatField()),
                ('AssocFee', models.FloatField()),
                ('EHS_Empl_share', models.FloatField()),
                ('Mar_Adv', models.FloatField()),
                ('FC', models.FloatField()),
                ('bFlaf_day_sub', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=20)),
                ('year', models.PositiveIntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('dayes', models.IntegerField()),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payroll.Employee')),
            ],
        ),
    ]
