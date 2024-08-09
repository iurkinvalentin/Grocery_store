from rest_framework import serializers
from products.models import Category, SubCategory, Product, Basket, BasketItem

MIN_AMOUNT = 1
MAX_AMOUNT = 2000


class SubCategorySerializer(serializers.ModelSerializer):
    """Сериализатор для подкатегорий товаров."""

    class Meta:
        model = SubCategory
        fields = ("name", "slug", "image", "parent_category")


class CategorySerializer(serializers.ModelSerializer):
    """Сериализатор для категорий товаров."""
    subcategories = SubCategorySerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ("name", "slug", "image", "subcategories")


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для продуктов."""
    category = serializers.CharField(
        source="subcategory.parent_category.name", read_only=True
    )
    subcategory = serializers.CharField(
        source="subcategory.name", read_only=True)
    images = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ("name", "slug", "price", "category", "subcategory", "images")

    def get_images(self, obj):
        return {
            "small": obj.image_small.url,
            "medium": obj.image_medium.url,
            "large": obj.image_large.url,
        }


class BasketItemSerializer(serializers.ModelSerializer):
    """Сериализатор для элемента корзины с продуктом и его количеством."""
    product = ProductSerializer(read_only=True)
    quantity = serializers.IntegerField(
        min_value=MIN_AMOUNT, max_value=MAX_AMOUNT)

    class Meta:
        model = BasketItem
        fields = ("id", "product", "quantity")


class BasketSerializer(serializers.ModelSerializer):
    """Сериализатор для корзины пользователя."""
    items = serializers.SerializerMethodField()
    total_quantity = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = Basket
        fields = ("items", "total_quantity", "total_price")

    def get_items(self, obj):
        return [item.product.name for item in obj.items.all()]

    def get_total_quantity(self, obj):
        return sum(item.quantity for item in obj.items.all())

    def get_total_price(self, obj):
        return sum(
            item.quantity * item.product.price for item in obj.items.all())
