# Generated by Django 4.1.7 on 2023-11-01 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_laptop_laptop_img1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=100)),
                ('qty', models.PositiveIntegerField()),
                ('price_per_unit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_phone', models.PositiveBigIntegerField()),
                ('customer_address', models.CharField(max_length=150)),
                ('customer_email', models.CharField(max_length=100)),
            ],
        ),
    ]
