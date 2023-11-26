from django.db import models

# Create your models here.

class MyUser(models.Model):
    
    ABONNE=""
    CREATEUR=""
    Administrateur=""
    
    ROLE = [
        (ABONNE, "Abonné"),
        (CREATEUR, "créateur"),
        (Administrateur, "Administrateur"),    
    ]
    
    first_name = models.CharField(max_length=3000)
    last_name = models.CharField(max_length=3000)
    date_of_birth = models.DateField('date_of_birth')
    role = models.CharField('role', max_length=50,choices=ROLE,default=ABONNE )
    
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    