# Generated by Django 2.2.7 on 2019-11-24 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("postcard", "0011_postcard_publish_date")]

    operations = [
        migrations.RemoveField(model_name="postcard", name="publish_date")
    ]
