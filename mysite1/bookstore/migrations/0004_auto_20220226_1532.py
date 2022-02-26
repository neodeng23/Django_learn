# Generated by Django 2.2.12 on 2022-02-26 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_auto_20220226_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='info',
        ),
        migrations.AddField(
            model_name='book',
            name='market_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7, verbose_name='定价'),
        ),
        migrations.AddField(
            model_name='book',
            name='pub',
            field=models.CharField(default='', max_length=100, verbose_name='出版商'),
        ),
    ]