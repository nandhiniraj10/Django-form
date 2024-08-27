from django.db import models

# Create your models here.
# class pyth(models.Model):
#    name=models.CharField(max_length=50)
#    char=models.CharField(max_length=50)

# models.py
# models.py
# yourappname/models.py

# from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()

    # def __str__(self):
    #     return f"{self.name},{self.age}"





