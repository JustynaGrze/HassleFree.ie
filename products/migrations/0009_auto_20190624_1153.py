# Generated by Django 2.0 on 2019-06-24 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20190624_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
