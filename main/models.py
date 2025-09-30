from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    thumbnail = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    # ForeignKey user, boleh kosong untuk data lama
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    # Tambahan field
    is_featured = models.BooleanField(default=False)
    best_seller = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)

    def is_new(self):
        return (timezone.now() - self.created_at).days <= 7

    def __str__(self):
        return self.name
