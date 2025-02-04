# Generated by Django 5.1.4 on 2025-01-21 05:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0001_initial'),
        ('Customer', '0002_feedback'),
        ('Shop', '0002_rename_content_brushbazaarproducts_artist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(default='my_address', max_length=300)),
                ('postal_zip', models.IntegerField()),
                ('delivery_status', models.BooleanField(default=False)),
                ('date_time', models.DateTimeField(auto_now=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('quantity', models.IntegerField(default=0)),
                ('payment_status', models.BooleanField(default=False)),
                ('payment_type', models.IntegerField(choices=[(1, 'Cash On Delivery'), (2, 'Card Payment')])),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Cart.cart')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customer.customerdetails')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('expiry_Month', models.CharField(max_length=2)),
                ('expiry_year', models.CharField(max_length=2)),
                ('cvv', models.CharField(max_length=3)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cart.order')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Shop.brushbazaarproducts')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('delivery_status', models.BooleanField(default=False)),
                ('product_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cart.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Shop.brushbazaarproducts')),
            ],
        ),
    ]
