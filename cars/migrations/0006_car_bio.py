# Generated by Django 5.0.4 on 2024-05-12 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_carinventory_cars_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
    ]
