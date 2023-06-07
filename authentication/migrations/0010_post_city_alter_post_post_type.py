# Generated by Django 4.2.1 on 2023-06-07 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_alter_post_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='city',
            field=models.CharField(default='Bishkek', max_length=255),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('Sale', 'Sale'), ('Rent', 'Rent')], default='Sale', max_length=10),
        ),
    ]
