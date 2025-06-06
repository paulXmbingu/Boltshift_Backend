# Generated by Django 5.2.1 on 2025-05-28 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0012_product_productfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productfile',
            name='product',
        ),
        migrations.AlterField(
            model_name='photosmodel',
            name='product_photos',
            field=models.ImageField(upload_to='Product_Photos/'),
        ),
        migrations.AlterField(
            model_name='videosmodel',
            name='product_videos',
            field=models.FileField(upload_to='Product_Videos/'),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='ProductFile',
        ),
    ]
