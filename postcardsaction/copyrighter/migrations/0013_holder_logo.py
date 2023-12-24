# Generated by Django 4.2.3 on 2023-08-30 10:25

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ("copyrighter", "0012_licence_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="holder",
            name="logo",
            field=stdimage.models.StdImageField(
                blank=True,
                force_min_size=False,
                upload_to="img/copyrightholder",
                variations={
                    "large": (1024, 1024),
                    "medium": (600, 600),
                    "small": (300, 300),
                    "thumbnail": (150, 150, False),
                },
            ),
        ),
    ]