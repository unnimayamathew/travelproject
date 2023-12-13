from django.db import models


# Create your models here.
class image(models.Model):
    def __str__(self):
     return self.name
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    disc = models.TextField()
    value=models.CharField(max_length=250)



