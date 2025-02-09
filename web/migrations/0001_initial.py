# Generated by Django 5.1.4 on 2024-12-05 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TimeStampedModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web.timestampedmodel')),
                ('name_ru', models.CharField(max_length=255, unique=True, verbose_name='Название на русском')),
                ('name_en', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Название на английском')),
                ('name_ch', models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Название на китайском')),
                ('order_id', models.SmallIntegerField(blank=True, default=10, null=True)),
            ],
            options={
                'verbose_name': 'Раздел меню',
                'verbose_name_plural': 'Разделы меню',
                'ordering': ('name_ru', 'order_id'),
            },
            bases=('web.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='web.timestampedmodel')),
                ('is_vegan', models.BooleanField(default=False, verbose_name='Вегетарианское меню')),
                ('is_special', models.BooleanField(default=False, verbose_name='Специальное предложение')),
                ('code', models.IntegerField(verbose_name='Код поставщика')),
                ('internal_code', models.IntegerField(blank=True, null=True, unique=True, verbose_name='Код в приложении')),
                ('name_ru', models.CharField(max_length=255, verbose_name='Название на русском')),
                ('description_ru', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание на русском')),
                ('description_en', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание на английском')),
                ('description_ch', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание на китайском')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('is_publish', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('additional', models.ManyToManyField(blank=True, related_name='additional_from', to='web.food', verbose_name='Дополнительные товары')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='food', to='web.foodcategory', verbose_name='Раздел меню')),
            ],
            bases=('web.timestampedmodel',),
        ),
    ]
