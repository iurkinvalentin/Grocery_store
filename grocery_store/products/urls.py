from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from products.views import (
    CategoryListView,
    ProductListView,
    BasketView,
    BasketItemView
)


urlpatterns = [
    path("api-token-auth/", obtain_auth_token, name="api_token_auth"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path("products/", ProductListView.as_view(), name="product-list"),
    path("basket/", BasketView.as_view(), name="basket"),
    path("basket/item/", BasketItemView.as_view(), name="basket-item"),
]
