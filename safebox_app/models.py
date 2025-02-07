from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Model(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='models')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
             self.slug = slugify(f"{self.brand.name}-{self.name}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.brand.name} - {self.name}"

class ModelImage(models.Model):
    model = models.ForeignKey(Model, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='model_images/')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']
    def __str__(self):
        return f"Rasm - {self.model.name} ({self.order})"

class Safe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dimensions = models.CharField(max_length=255, blank=True)
    weight = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    material = models.CharField(max_length=255, blank=True)
    lock_type = models.CharField(max_length=255, blank=True)
    fire_resistance = models.CharField(max_length=255, blank=True)
    warranty = models.CharField(max_length=255, blank=True)
    is_available = models.BooleanField(default=True)
    features = models.TextField(blank=True)
    quantity = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True, blank=True, related_name='safes')
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.slug])

    def __str__(self):
        return self.name

class Review(models.Model):
    safe = models.ForeignKey(Safe, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review by {self.user.username} for {self.safe.name}"