# Generated by Django 3.1.7 on 2021-03-18 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postcard", "0002_auto_20210313_1529"),
    ]

    operations = [
        migrations.AddField(
            model_name="postcard",
            name="subtitle",
            field=models.CharField(
                blank=True,
                help_text="A subtitle for the postcard",
                max_length=100,
                null=True,
            ),
        ),
    ]
