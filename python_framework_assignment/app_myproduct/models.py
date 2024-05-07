from django.db import models

# Create your models here.
class Category(models.Model):

    catname = models.CharField(max_length=20)

    def __str__(self):
        return self.catname
    

class Product(models.Model):
    
    pname = models.CharField(max_length=20)
    price = models.IntegerField()
    qty = models.IntegerField()
    # category = models.ForeignKey(Category,on_delete=models.CASCADE)
    ram = models.IntegerField(default=0)
    