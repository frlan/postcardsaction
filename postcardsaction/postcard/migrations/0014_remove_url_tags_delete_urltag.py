# Generated by Django 5.0 on 2023-12-24 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("postcard", "0013_alter_url_unique_together"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="url",
            name="tags",
        ),
        migrations.DeleteModel(
            name="URLTag",
        ),
    ]