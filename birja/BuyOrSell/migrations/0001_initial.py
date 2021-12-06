# Generated by Django 3.2.9 on 2021-12-06 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoCurrencyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='currency name')),
                ('dollar_price', models.FloatField(max_length=10, verbose_name='price in dollars')),
                ('euro_price', models.FloatField(max_length=10, verbose_name='price in euros')),
                ('rubles_price', models.FloatField(max_length=16, verbose_name='price in rubles')),
                ('logo', models.ImageField(upload_to='', verbose_name='logo')),
                ('description', models.TextField(max_length=200, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencies',
            },
        ),
    ]
