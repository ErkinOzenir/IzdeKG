# Generated by Django 4.2.1 on 2023-06-07 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_post_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='images',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='authentication.attachment'),
        ),
    ]