# Generated by Django 5.0.2 on 2024-03-14 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_remove_customer_profile_pic_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Indoor', 'Indoor'), ('Out Door', 'Out Door'), ('Management Software', 'Management Software')], max_length=200, null=True),
        ),
    ]
