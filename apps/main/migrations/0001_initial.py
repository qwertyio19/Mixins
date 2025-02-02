# Generated by Django 5.1.5 on 2025-02-01 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название товара')),
                ('description', models.TextField(max_length=255, verbose_name='Описание')),
                ('color', models.CharField(max_length=255, verbose_name='Цвет')),
                ('size', models.CharField(max_length=255, verbose_name='Размер')),
                ('price', models.IntegerField(verbose_name='Цена')),
                ('old_price', models.IntegerField(verbose_name='Старая цена')),
                ('quantity', models.IntegerField(blank=True, null=True, verbose_name='Количество продуктов')),
                ('created_at', models.DateTimeField(verbose_name='Дата создания')),
            ],
            options={
                'verbose_name': 'Продукты',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Категория')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.product', verbose_name='Продукты')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категория',
            },
        ),
    ]
