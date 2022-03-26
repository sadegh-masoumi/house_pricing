# Generated by Django 4.0.3 on 2022-03-26 09:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.PositiveIntegerField()),
                ('room', models.PositiveSmallIntegerField()),
                ('has_parking', models.BooleanField()),
                ('has_warehouse', models.BooleanField()),
                ('has_elevator', models.BooleanField()),
                ('price', models.FloatField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_apartment.address')),
            ],
        ),
    ]
