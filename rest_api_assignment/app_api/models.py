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
    category = models.ForeignKey(Category,on_delete=models.CASCADE)




    # book - author..abs

class Author(models.Model):

            aname = models.CharField(max_length=20)

            def __str__(self):
                return self.aname


class Book(models.Model):
            book_name = models.CharField(max_length=20)
            price = models.IntegerField()
            qty = models.IntegerField()
            author_name = models.ForeignKey(Author,on_delete=models.CASCADE)

