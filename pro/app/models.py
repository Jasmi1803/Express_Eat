from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    message=models.TextField()
    def __str__(self) :
        return f'Message from {self.name}'