# Generated by Django 2.2.13 on 2020-06-07 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copyrighter', '0005_auto_20200526_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='copyright',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]