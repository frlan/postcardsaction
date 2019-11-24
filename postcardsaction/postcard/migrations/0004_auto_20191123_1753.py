# Generated by Django 2.2.7 on 2019-11-23 17:53

from django.db import migrations, models
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [("postcard", "0003_postcard_some_textfiled")]

    operations = [
        migrations.RemoveField(model_name="postcard", name="some_textfiled"),
        migrations.AlterField(
            model_name="postcard",
            name="description",
            field=django_markdown.models.MarkdownField(
                default="",
                help_text="Actual description for a postcard:\n\t\t\t* some story behind\n\t\t\t* where came it from\n\t\t\t* what to see",
            ),
        ),
        migrations.AlterField(
            model_name="postcard",
            name="description_short",
            field=models.CharField(
                default="",
                help_text="Short description of the card may be used as a teaser",
                max_length=100,
            ),
        ),
    ]
