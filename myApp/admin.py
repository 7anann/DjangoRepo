from django.contrib import admin
from .models import CustomUser
from .models import Profile  # Import your Profile model


# Register your models here.

admin.site.register(CustomUser)

admin.site.register(Profile)  # Register it so it shows up
