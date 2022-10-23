# Generated by Django 4.1.2 on 2022-10-23 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("copyrighter", "0010_licence_commercial"),
    ]

    operations = [
        migrations.AddField(
            model_name="copyright",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AddField(
            model_name="copyright",
            name="url",
            field=models.URLField(blank=True),
        ),
    ]
