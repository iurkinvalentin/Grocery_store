# Generated by Django 5.1 on 2024-08-09 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ImageField(upload_to="media/", verbose_name="Изображение"),
        ),
        migrations.AlterField(
            model_name="product",
            name="image_large",
            field=models.ImageField(
                upload_to="media/large/", verbose_name="Большое изображение"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image_medium",
            field=models.ImageField(
                upload_to="media/medium/", verbose_name="Среднее изображение"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image_small",
            field=models.ImageField(
                upload_to="media/small/", verbose_name="Маленькое изображение"
            ),
        ),
        migrations.AlterField(
            model_name="subcategory",
            name="image",
            field=models.ImageField(upload_to="media/", verbose_name="Изображение"),
        ),
    ]