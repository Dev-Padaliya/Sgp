# Generated by Django 4.1.6 on 2023-04-04 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank='True', null='True', upload_to='items_images'),
        ),
    ]
