# Generated by Django 4.1 on 2022-08-13 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_essays_created"),
    ]

    operations = [
        migrations.AddField(
            model_name="essays",
            name="upload_image",
            field=models.ImageField(default="surface.jpg", upload_to="upload/"),
        ),
    ]