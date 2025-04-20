from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Gender(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class CustomerType(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class ProductLine(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Payment(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name

class SuperMarketSales(models.Model):
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    customer_type = models.ForeignKey(CustomerType, on_delete=models.CASCADE)
    product_line = models.ForeignKey(ProductLine, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)  # Added branch relationship instead of self-reference
    
    def __str__(self):
        return f"Sale {self.id} - {self.product_line} - {self.date}"