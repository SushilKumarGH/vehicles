# Generated by Django 3.2.9 on 2022-01-25 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('Bike', 'bike'), ('Car', 'car'), ('Zeep', 'zeep'), ('Bus', 'bus'), ('Truck', 'truck')], default='None', max_length=10)),
                ('Number', models.CharField(max_length=10)),
                ('Status', models.BooleanField()),
                ('Speed', models.FloatField()),
                ('Averagespeed', models.FloatField()),
                ('Temperature', models.FloatField()),
                ('Fuellevel', models.FloatField()),
                ('Enginestatus', models.CharField(choices=[('Above Average', 'Above Average'), ('Average', 'Average'), ('Below Average', 'Below Average')], default='None', max_length=20)),
            ],
        ),
    ]