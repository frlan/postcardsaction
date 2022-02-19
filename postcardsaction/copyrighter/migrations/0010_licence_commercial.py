# Generated by Django 4.0.1 on 2022-02-12 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copyrighter', '0009_rename_org_name_holder_orig_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='licence',
            name='commercial',
            field=models.BooleanField(default=False, help_text='Whether allowed to use it commercial as e.g. for Public Domain or CC without NC-attribution'),
        ),
    ]