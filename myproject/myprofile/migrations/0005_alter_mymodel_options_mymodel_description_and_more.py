# Generated by Django 5.0.6 on 2024-06-19 11:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myprofile", "0004_contact_mymodel"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mymodel",
            options={},
        ),
        migrations.AddField(
            model_name="mymodel",
            name="description",
            field=models.CharField(
                blank=True, default="No description provided", max_length=255
            ),
        ),
        migrations.AddField(
            model_name="mymodel",
            name="file",
            field=models.FileField(default="uploads/default.pdf", upload_to="uploads/"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="mymodel",
            name="uploaded_at",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="blog",
            name="author",
            field=models.CharField(default="Anonymous", max_length=100),
        ),
        migrations.AlterField(
            model_name="blog",
            name="date_posted",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="blog",
            name="title",
            field=models.CharField(default="Untitled", max_length=200),
        ),
        migrations.AlterField(
            model_name="contact",
            name="created_at",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(default="example@example.com", max_length=254),
        ),
        migrations.AlterField(
            model_name="contact",
            name="message",
            field=models.TextField(default="No message"),
        ),
        migrations.AlterField(
            model_name="contact",
            name="name",
            field=models.CharField(default="John Doe", max_length=100),
        ),
        migrations.AlterField(
            model_name="contact",
            name="subject",
            field=models.CharField(default="No Subject", max_length=200),
        ),
    ]
