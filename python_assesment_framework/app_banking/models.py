from django.db import models

# Create your models here.
class Roles(models.Model):
    role_name =models.CharField(max_length=100)

    def __str__(self):
        return self.role_name
    


class User(models.Model):
    role = models.ForeignKey(Roles,on_delete=models.CASCADE)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    balance = models.IntegerField(default=0)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.username
    




    
        