from django.db import models
from autoslug import AutoSlugField
# Create your models here.

class Product(models.Model):
    # product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50)
    product_price=models.IntegerField(default=0)
    product_discription=models.CharField(max_length=100)
    product_category=models.CharField(max_length=50,default="")
    product_image=models.ImageField(upload_to="shop/images")
    product_slug = AutoSlugField(populate_from='product_name',unique=True,null=True,default=None)

    def __str__(self):
        return self.product_name
    
