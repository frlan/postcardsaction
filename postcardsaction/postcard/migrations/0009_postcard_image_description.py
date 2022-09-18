# Generated by Django 4.0.1 on 2022-01-14 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postcard", "0008_rename_description_text_postcard_backside_description_text"),
    ]

    operations = [
        migrations.AddField(
            model_name="postcard",
            name="image_description",
            field=models.TextField(
                blank=True,
                help_text="\n            A more formal description of the image for visual\n            handicapped people -- a description that might not fit to\n            the main text\n        ",
                null=True,
            ),
        ),
    ]
