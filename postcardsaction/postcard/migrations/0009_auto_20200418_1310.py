# Generated by Django 2.2.10 on 2020-04-18 13:10

from django.db import migrations
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ("postcard", "0008_auto_20200418_1259"),
    ]

    operations = [
        migrations.AlterField(
            model_name="url",
            name="tags",
            field=tagulous.models.fields.TagField(
                _set_tag_meta=True,
                force_lowercase=False,
                help_text="Enter a comma-separated tag string",
                to="postcard.URLTag",
                tree=True,
            ),
        ),
    ]
