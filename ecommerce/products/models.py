from django.db import models


# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name


class SubCategories(models.Model):
    name = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='category')

    class Meta:
        db_table = "sub_categories"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE, related_name='subcategory')

    class Meta:
        db_table = "products"

    def __str__(self):
        return self.name
