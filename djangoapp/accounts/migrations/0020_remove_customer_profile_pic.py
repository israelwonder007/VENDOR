# Generated by Django 5.0.2 on 2024-03-19 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_customer_profile_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='profile_pic',
        ),
    ]
