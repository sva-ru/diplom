# Generated by Django 5.0.1 on 2024-02-20 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_partnerimport_alter_order_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='partnerimport',
            options={'verbose_name': 'Импорт товаров', 'verbose_name_plural': 'Импорт товаров'},
        ),
    ]
