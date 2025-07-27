from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    document = models.FileField(upload_to='file/')
    passw= models.CharField(max_length=50)
    c_passw =models.CharField(max_length=50)


class Query(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    query = models.TextField()

    def __str__(self):
        return self.name
