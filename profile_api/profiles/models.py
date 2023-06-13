from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    
    def __str__(self):
        return self.name

