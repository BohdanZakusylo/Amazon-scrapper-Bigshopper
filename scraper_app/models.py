from django.db import models


# Model for storing product information
class Product(models.Model):
    asin = models.CharField(max_length=255, null=True, default=None)  # ASIN (Amazon Standard Identification Number)
    gtin = models.CharField(max_length=255, null=True, default=None)  # GTIN (Global Trade Item Number)
    link = models.CharField(max_length=255, null=True, default=None)  # URL link to the product
    productTitle = models.CharField(max_length=255, null=True, default=None)  # Title of the product
    timeStamp = models.DateTimeField(auto_now_add=True)  # Timestamp when the record is created
    sellerName = models.CharField(max_length=255, null=True, default=None)  # Name of the seller or distributor


# Model for storing price information related to a product
class Price(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to the related product
    originalPrice = models.CharField(max_length=255, null=True, default=None)  # Original price
    salePrice = models.CharField(max_length=255, null=True, default=None)  # Sale price
    shippingPrice = models.CharField(max_length=255, null=True, default=None)  # Shipping price


# Model for storing product specifications related to a product
class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to the related product
    specification = models.JSONField(null=True, default=None)  # Product specifications in JSON format
    sellerName = models.CharField(max_length=255, null=True, default=None)  # Name of the seller or distributor


# Model for storing information about other distributors of a product
class OtherDistributors(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Link to the related product
    normal_price = models.CharField(max_length=255, null=True, default=None)  # Normal price from other distributors
    sold_by = models.CharField(max_length=255, null=True, default=None)  # Name of the distributor or seller
