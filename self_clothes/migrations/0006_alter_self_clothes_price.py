# Generated by Django 4.1.3 on 2022-11-21 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('self_clothes', '0005_alter_self_clothes_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='self_clothes',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
