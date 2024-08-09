from django.contrib import admin

from products.models import Category, SubCategory, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ("name", "subcategory", "price")
    list_filter = ("subcategory", "subcategory__parent_category")
