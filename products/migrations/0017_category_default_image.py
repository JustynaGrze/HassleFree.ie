# Generated by Django 2.0 on 2019-06-27 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_remove_product_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='default_image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
