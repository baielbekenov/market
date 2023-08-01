# Generated by Django 4.2.3 on 2023-08-01 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0008_remove_goods_amount_goods_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='total_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Общая цена'),
        ),
    ]