# Generated by Django 5.1.1 on 2024-09-29 11:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("store", "0002_book_cover_image"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="book",
            name="cover_image",
        ),
        migrations.RemoveField(
            model_name="book",
            name="created_at",
        ),
        migrations.AddField(
            model_name="book",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="book_images/"),
        ),
        migrations.AlterField(
            model_name="book",
            name="stock",
            field=models.IntegerField(),
        ),
    ]
