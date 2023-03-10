# Generated by Django 4.1.7 on 2023-02-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_menu_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="place",
            name="color",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="place",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="place",
            name="font",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="place",
            name="image",
            field=models.URLField(
                default="https://media.timeout.com/images/105802468/750/562/image.jpg",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="place",
            name="number_of_tables",
            field=models.IntegerField(default=1),
        ),
    ]
