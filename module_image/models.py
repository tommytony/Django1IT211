from django.db import models

# Create your models here.

class Post(models.Model):
    titled=models.CharField(max_length=3000)
    photo=models.ImageField(upload_to="images/")
    description=models.TextField()
    
    def __str__(self):
        return self.titled