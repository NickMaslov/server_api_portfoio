# Generated by Django 4.1.7 on 2023-02-23 06:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_online_store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="brand",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="category",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="countInStock",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="product",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.URLField(
                default="https://content.optimumnutrition.com/i/on/on-C100969_Image_01",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="numReviews",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=7, null=True
            ),
        ),
        migrations.AddField(
            model_name="product",
            name="rating",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=7, null=True
            ),
        ),
    ]