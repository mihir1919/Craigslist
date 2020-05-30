from django.db import models
from django.utils.timezone import timezone
from datetime import date
CAT_CHOICES = (
    ('car','CAR'),
    ('home', 'Furniture'),
    ('education','EDUCATION'),
    ('electronics','ELECTRONICS'),
    ('misc','MISC'),
)

# Create your models here.
class item(models.Model):
    name=models.CharField(max_length=200)
    category = models.CharField(max_length=100, choices=CAT_CHOICES, default='misc')
    price=models.IntegerField()
    desc=models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    state= models.CharField(max_length=200)
    city=models.CharField(max_length=200)
    img=models.ImageField(null=True)
    author=models.CharField(max_length=100,null=False)

    def __str__(self):
        return self.name

class Carts(models.Model):
    author=models.CharField(max_length=100,null=False)
    image=models.ImageField(null=True)
    name=models.ForeignKey(item,on_delete=models.CASCADE)
    date=models.DateTimeField(null=True)

    def __str__(self):
        return str(self.name)