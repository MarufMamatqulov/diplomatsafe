from django.contrib import admin
from .models import Brand, Category, Model, ModelImage, Safe, Review

class ModelImageInline(admin.TabularInline):
    model = ModelImage
    min_num = 0  # Kamida 0 ta rasm (bo'sh bo'lishi mumkin)
    max_num = 8  # Ko'pi bilan 8 ta rasm


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'slug')
    inlines = [ModelImageInline]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Safe)
class SafeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'model', 'is_available', 'slug')
    list_filter = ('is_available', 'category', 'model__brand')
    search_fields = ('name', 'description', 'model__name')
    prepopulated_fields = {'slug': ('name',)}


# @admin.register(Review)
# class ReviewAdmin(admin.ModelAdmin):
#     list_display = ('safe', 'rating', 'user', 'created_date')