# Generated by Django 4.1.7 on 2023-11-01 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptop',
            name='laptop_img1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
