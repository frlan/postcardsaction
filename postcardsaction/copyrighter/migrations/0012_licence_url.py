# Generated by Django 4.1.2 on 2022-10-23 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("copyrighter", "0011_copyright_description_copyright_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="licence",
            name="url",
            field=models.URLField(blank=True),
        ),
    ]
