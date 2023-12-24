# Generated by Django 4.1.2 on 2022-12-29 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("poi", "0002_alter_poi_urls"),
        ("postcard", "0010_alter_postcard_image_alter_series_logo"),
    ]

    operations = [
        migrations.AddField(
            model_name="postcard",
            name="poi",
            field=models.ManyToManyField(blank=True, null=True, to="poi.poi"),
        ),
    ]