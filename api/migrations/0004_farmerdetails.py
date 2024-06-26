# Generated by Django 5.0.2 on 2024-04-10 09:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_customuser_user_image_alter_product_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FarmerDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('overallrating', models.CharField(max_length=5)),
                ('farms', models.TextField()),
                ('Verified', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.customuser')),
            ],
        ),
    ]
