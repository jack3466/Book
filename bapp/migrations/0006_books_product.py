# Generated by Django 4.2.7 on 2023-11-24 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bapp', '0005_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='product',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
