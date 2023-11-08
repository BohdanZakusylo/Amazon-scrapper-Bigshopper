# Generated by Django 4.2.6 on 2023-11-03 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asin', models.CharField(default=None, max_length=255, null=True)),
                ('gtin', models.CharField(default=None, max_length=255, null=True)),
                ('link', models.CharField(default=None, max_length=255, null=True)),
                ('productTitle', models.CharField(default=None, max_length=255, null=True)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('sellerName', models.CharField(default=None, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification', models.JSONField(default=None, null=True)),
                ('sellerName', models.CharField(default=None, max_length=255, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originalPrice', models.CharField(default=None, max_length=255, null=True)),
                ('salePrice', models.CharField(default=None, max_length=255, null=True)),
                ('shippingPrice', models.CharField(default=None, max_length=255, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper_app.product')),
            ],
        ),
        migrations.CreateModel(
            name='OtherDistributors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('normal_price', models.CharField(default=None, max_length=255, null=True)),
                ('sold_by', models.CharField(default=None, max_length=255, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scraper_app.product')),
            ],
        ),
    ]