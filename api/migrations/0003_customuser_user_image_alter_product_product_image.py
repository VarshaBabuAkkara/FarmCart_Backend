# Generated by Django 5.0.2 on 2024-03-30 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_product_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/user'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/products'),
        ),
    ]
