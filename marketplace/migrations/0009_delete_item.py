# Generated by Django 4.2.2 on 2023-06-22 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0008_product_image_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Item',
        ),
    ]