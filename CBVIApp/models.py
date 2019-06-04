from django.db import models
from django.urls import reverse
# Create your models here.
class Product(models.Model):
        pid=models.PositiveIntegerField()
        pname=models.CharField(max_length=30)
        category=models.CharField(max_length=30)
        price=models.FloatField()
        description=models.TextField()
        image=models.FileField(upload_to="images/")
        def get_absolute_url(self):
	           return reverse('detail',kwargs={'pk':self.pk})

class Cart(models.Model):
    pid=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    user=models.CharField(max_length=30,default=None)
    image=models.CharField(max_length=80,default=None)
    price=models.FloatField(default=None)
    total=models.FloatField(default=None)
