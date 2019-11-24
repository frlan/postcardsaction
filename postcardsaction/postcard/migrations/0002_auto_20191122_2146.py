# Generated by Django 2.2.7 on 2019-11-22 21:46

import datetime
from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [("postcard", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="postcard",
            name="description_short",
            field=django_markdown.models.MarkdownField(default=""),
        ),
        migrations.AddField(
            model_name="postcard",
            name="swapping",
            field=models.BooleanField(
                default=False,
                help_text="Whether this postcard is free for private swapping",
            ),
        ),
        migrations.AddField(
            model_name="postcard",
            name="year_recieved",
            field=models.DateField(
                default=datetime.date.today, verbose_name="Date"
            ),
        ),
        migrations.AddField(
            model_name="postcard",
            name="year_verified",
            field=models.BooleanField(
                default=True,
                help_text="Whether the year of recieving is verified",
            ),
        ),
        migrations.AlterField(
            model_name="postcard",
            name="description",
            field=django_markdown.models.MarkdownField(default=""),
        ),
    ]
