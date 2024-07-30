from django.db import models

# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=100,blank=False, null=False)
    email=models.EmailField(blank=False, null=False)
    phone=models.CharField(max_length=15,blank=False, null=False)
    subject=models.CharField(max_length=200,blank=False, null=False)
    message=models.CharField(max_length=1000,blank=False, null=False)

    def __str__(self):
        return self.name
    
from django.db import models

class booking(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)
    phone = models.CharField(max_length=15, blank=False, null=False)
    date = models.DateField(null=False)
    time = models.TimeField(null=False, default='00:00:00')  # Default time value
    disease = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name
    


class NewsletterSubscription(models.Model):
    email = models.EmailField(unique=True,max_length=254)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.email 



