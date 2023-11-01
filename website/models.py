from django.db import models

# Create your models here.
class Laptop(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.PositiveIntegerField()
    #other details
    ram = models.CharField(max_length=100)
    chipset = models.CharField(max_length=100)
    storage = models.CharField(max_length=100)
    processor = models.CharField(max_length=100)
    graphics = models.CharField(max_length=100)
    operating_sys = models.CharField(max_length=100)
    laptop_img1 = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return(f"{self.brand} {self.model}")