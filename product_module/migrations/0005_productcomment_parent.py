# Generated by Django 5.0.6 on 2024-06-26 15:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0004_productcomment_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcomment',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product_module.productcomment', verbose_name='والد'),
        ),
    ]
