from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=100,default="None")
    email = models.EmailField(max_length=50,default="None")
    address = models.CharField(max_length=500,default="None")

    def __str__(self):
        return self.name
    

