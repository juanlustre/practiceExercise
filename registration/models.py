from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=150)
    date_registered = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=16)

    profile_picture = models.ImageField(
        upload_to='profile_pictures/',
        blank=True,        
        null=True          
    )
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"