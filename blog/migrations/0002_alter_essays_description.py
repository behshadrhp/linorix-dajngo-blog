# Generated by Django 4.1 on 2022-08-14 11:56

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="essays",
            name="description",
            field=django_quill.fields.QuillField(),
        ),
    ]
