# Generated by Django 5.2.1 on 2025-05-30 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0023_option1model_option2model_delete_optionsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SummaryDescriptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary_description', models.TextField(verbose_name='Summary Description')),
            ],
            options={
                'verbose_name': 'Summary Description',
                'verbose_name_plural': 'Summary Description',
            },
        ),
        migrations.RemoveField(
            model_name='detailmodel',
            name='product_summary',
        ),
    ]
