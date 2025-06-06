# Generated by Django 5.2.1 on 2025-05-29 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0017_reviewmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryMeterModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remaining_items', models.IntegerField(verbose_name='Remaining Items')),
                ('total_items', models.IntegerField(verbose_name='Total Items')),
            ],
            options={
                'verbose_name': 'Inventory Meter',
                'verbose_name_plural': 'Inventory Meters',
            },
        ),
    ]
