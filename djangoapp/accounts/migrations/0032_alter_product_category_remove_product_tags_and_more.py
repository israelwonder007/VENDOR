# Generated by Django 5.0.2 on 2024-03-21 09:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_rename_descirption_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('PRIMARK', 'PRIMARK'), ('Electronics', 'Electronics'), ('Books', 'Books'), ('Management Software', 'Management Software')], max_length=200, null=True),
        ),
        migrations.RemoveField(
            model_name='product',
            name='tags',
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.tag'),
        ),
    ]
