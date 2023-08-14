from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/',blank=True, null=True)

    def __str__(self):
        return self.name
    
    # class Meta:
    #     ordering = ['-id']

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)   
    price = models.PositiveIntegerField()
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']
