from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# myApp/models.py


class Product(models.Model):
    name = models.CharField(max_length=100)  # A short text field
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Numbers
    description = models.TextField()  # Long text
    created_at = models.DateTimeField(auto_now_add=True)  # Date/Time


class CustomUser(AbstractUser):
    # Add your extra fields here
    phone_number = models.CharField(max_length=15, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.email


from django.conf import settings  # Best practice to refer to the User model


# 2. The Profile Model (The Extension)
class Profile(models.Model):
    # Link to the User - ONLY defined here!
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # Extra fields that aren't in the default User model
    bio = models.TextField(max_length=500, blank=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True)
    website = models.URLField(blank=True)

    def __str__(self):
        return f"Profile for {self.user.username}"


class Post(models.Model):
    class Meta:
        ordering = ["-id"]  # This tells Django: "Always show newest first"

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1
    )
    title = models.CharField(max_length=100)
    content = models.TextField()
    author_email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
