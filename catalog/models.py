from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.CharField(max_length=250, blank=True, verbose_name="Descrição")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nome")
    description = models.CharField(max_length=250, blank=True, verbose_name="Descrição")
    value = models.FloatField(verbose_name="Valor")
    image = models.ImageField(
        upload_to="products/main/", verbose_name="Imagem Principal"
    )
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="products/multiple/")
    description = models.CharField(
        max_length=250, blank=True, verbose_name="Descrição da Imagem"
    )

    def __str__(self):
        return f"Imagem de {self.product.name}"
