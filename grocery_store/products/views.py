from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import Category, Product, Basket, BasketItem
from products.serializers import (
    CategorySerializer,
    ProductSerializer,
    BasketSerializer,
    BasketItemSerializer,
)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from .pagination import CategoryPagination


class CategoryListView(generics.ListAPIView):
    """Получение списка категорий."""
    permission_classes = [AllowAny]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = PageNumberPagination


class ProductListView(generics.ListAPIView):
    """Получение списка продуктов."""
    permission_classes = [AllowAny]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = CategoryPagination


class BasketView(APIView):
    """Работа с корзиной пользователя."""

    def get(self, request):
        basket, created = Basket.objects.get_or_create(user=request.user)
        if not basket.items.exists():
            return Response(
                {"message": "Корзина пуста"}, status=status.HTTP_200_OK)
        serializer = BasketSerializer(basket)
        return Response(serializer.data)

    def delete(self, request):
        basket, created = Basket.objects.get_or_create(user=request.user)
        basket.items.all().delete()
        return Response(
            {"status": "Корзина пуста"}, status=status.HTTP_204_NO_CONTENT)


class BasketItemView(APIView):
    """Управление элементами корзины."""

    def post(self, request):
        basket, created = Basket.objects.get_or_create(user=request.user)
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity", 1)
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response(
                {"error": "Продукт не найден"},
                status=status.HTTP_404_NOT_FOUND
            )
        item, created = BasketItem.objects.get_or_create(
            basket=basket, product=product)
        item.quantity += quantity
        item.save()
        serializer = BasketItemSerializer(item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, request):
        basket, created = Basket.objects.get_or_create(user=request.user)
        product_id = request.data.get("product_id")
        quantity = request.data.get("quantity")
        try:
            item = BasketItem.objects.get(basket=basket, product_id=product_id)
        except BasketItem.DoesNotExist:
            return Response(
                {"error": "Продукт не найден"},
                status=status.HTTP_404_NOT_FOUND
            )
        item.quantity = quantity
        item.save()
        serializer = BasketItemSerializer(item)
        return Response(serializer.data)

    def delete(self, request):
        basket, created = Basket.objects.get_or_create(user=request.user)
        product_id = request.data.get("product_id")
        try:
            item = BasketItem.objects.get(basket=basket, product_id=product_id)
        except BasketItem.DoesNotExist:
            return Response(
                {"error": "Продукт не найден в корзине"},
                status=status.HTTP_404_NOT_FOUND,
            )

        item.delete()
        return Response(
            {"message": "Продукт удален из корзины"},
            status=status.HTTP_204_NO_CONTENT
        )
