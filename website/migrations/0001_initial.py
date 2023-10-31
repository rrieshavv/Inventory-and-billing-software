# Generated by Django 4.1.7 on 2023-10-30 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Laptop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('qty', models.PositiveIntegerField()),
                ('ram', models.CharField(max_length=100)),
                ('chipset', models.CharField(max_length=100)),
                ('storage', models.CharField(max_length=100)),
                ('processor', models.CharField(max_length=100)),
                ('graphics', models.CharField(max_length=100)),
                ('operating_sys', models.CharField(max_length=100)),
            ],
        ),
    ]
