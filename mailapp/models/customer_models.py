from django.db import models

class customer(models.Model):
    company=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    book=models.CharField(max_length=100)
    mail=models.EmailField()
   
    def __str__(self):
        return self.company