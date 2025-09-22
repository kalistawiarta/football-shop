from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=120)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=50)
    is_featured = models.BooleanField(default=False)

    # tambahan
    stock = models.PositiveIntegerField(default=0, blank=True)
    brand = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
    
