# Generated by Django 2.2.2 on 2019-06-11 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dolar',
            fields=[
                ('date', models.DateField(max_length=10, primary_key=True, serialize=False)),
                ('val', models.DecimalField(decimal_places=2, max_digits=7)),
                ('delta', models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True)),
            ],
        ),
    ]