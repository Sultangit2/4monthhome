from django.db import models


class Product(models.Model):
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=260)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    rate = models.FloatField(default=0)

    def __str__(self):
        return self.title

class Comment(models.Model):
    text = models.CharField(max_length=256)
    phones = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.phones.title}-{self.text}'


