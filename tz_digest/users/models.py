from django.db import models
from django.contrib.auth.models import AbstractUser

# users: Manage user registration, authentication, profiles, and permissions.


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True) # not a required field
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

    # When scaling up, use more sophisticated and scalable methods to store and serve user profile pictures. 
    # Instead of storing the images directly on the server's filesystem, they commonly use cloud storage 
    # services like Amazon S3, Google Cloud Storage, or Azure Blob Storage. These services provide several benefits, 
    # including scalability, reliability, and the ability to serve images through a content delivery network (CDN) 
    # for faster access. --> strategy used by Google
    
    def __str__(self):
        return self.username
