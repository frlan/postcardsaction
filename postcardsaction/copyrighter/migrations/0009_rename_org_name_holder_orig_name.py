# Generated by Django 3.2 on 2021-04-09 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("copyrighter", "0008_holder_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="holder",
            old_name="org_name",
            new_name="orig_name",
        ),
    ]
