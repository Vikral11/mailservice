from django.db import models

# Create your models here.
class data(models.Model):
    
    email= models.CharField(max_length=400)
    mail= models.CharField(max_length=1000000)
    mail_list=models.CharField(max_length=100000)

    def __str__(self):
        return (f"ID:{self.id},Email:{self.email}")