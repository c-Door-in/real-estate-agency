# Generated by Django 2.2.24 on 2022-02-14 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20220211_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='floor',
            field=models.CharField(db_index=True, help_text='Первый этаж, последний этаж, пятый этаж', max_length=3, verbose_name='Этаж'),
        ),
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(db_index=True, verbose_name='Новостройка'),
        ),
    ]
