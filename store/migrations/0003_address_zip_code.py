# Generated by Django 5.0.4 on 2024-04-24 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip_code',
            field=models.CharField(default='-', max_length=255),
            preserve_default=False,
        ),
    ]