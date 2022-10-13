from contextlib import nullcontext
from django.db import models
from api.category.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200)
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    price = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)  # is product featured?
    #category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    category = models.ManyToManyField(Category, blank=False)
    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}"

    @property
    def is_featured(self):
        return self.featured

    @property
    def is_available(self):
        return self.quantity > 0

    def set_featured(self, status):
        self.featured = status
        return self.save()
