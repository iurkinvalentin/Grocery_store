from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Модель для категорий товаров."""
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    image = models.ImageField(upload_to="media/", verbose_name="Изображение")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    """Модель для подкатегорий товаров."""
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    image = models.ImageField(upload_to="media/", verbose_name="Изображение")
    parent_category = models.ForeignKey(
        Category,
        related_name="subcategories",
        on_delete=models.CASCADE,
        verbose_name="Родительская категория",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Product(models.Model):
    """Модель для продуктов."""
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(unique=True, verbose_name="Slug")
    image_small = models.ImageField(
        upload_to="media/small/", verbose_name="Маленькое изображение"
    )
    image_medium = models.ImageField(
        upload_to="media/medium/", verbose_name="Среднее изображение"
    )
    image_large = models.ImageField(
        upload_to="media/large/", verbose_name="Большое изображение"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(
        Category,
        related_name="product",
        on_delete=models.CASCADE,
        verbose_name="Категория",
    )
    subcategory = models.ForeignKey(
        SubCategory,
        related_name="products",
        on_delete=models.CASCADE,
        verbose_name="Подкатегория",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Basket(models.Model):
    """Модель для корзины пользователя."""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="basket",
        verbose_name="Пользователь",
    )

    def __str__(self):
        return f"Корзина пользователя {self.user.username}"

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class BasketItem(models.Model):
    """Модель для элементов в корзине пользователя."""
    basket = models.ForeignKey(
        Basket, related_name="items",
        on_delete=models.CASCADE, verbose_name="Корзина"
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE,
        verbose_name="Продукт"
    )
    quantity = models.PositiveIntegerField(
        default=1, verbose_name="Количество")

    def __str__(self):
        return (
            f"{self.quantity} x {self.product.name} "
            "в корзине пользователя "
            f"{self.basket.user.username}"
        )

    class Meta:
        verbose_name = "Элемент корзины"
        verbose_name_plural = "Элементы корзины"
