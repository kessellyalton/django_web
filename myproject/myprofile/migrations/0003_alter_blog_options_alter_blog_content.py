# Generated by Django 5.0.6 on 2024-06-17 12:22

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("myprofile", "0002_blog_image"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blog",
            options={"ordering": ["-date_posted"]},
        ),
        migrations.AlterField(
            model_name="blog",
            name="content",
            field=django_ckeditor_5.fields.CKEditor5Field(verbose_name="Content"),
        ),
    ]
