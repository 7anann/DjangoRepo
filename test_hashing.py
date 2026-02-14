import os
import django

# Replace 'myProject' with your actual project folder name!
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

# --- YOUR CODE GOES HERE ---
from django.test import TestCase
from myApp.models import CustomUser
from django.contrib.auth.hashers import check_password


class HashingDemoTest(TestCase):
    def test_hashing_logic(self):
        # 1. CREATE the user the "Short Way"
        # create_user automatically calls set_password() for you!
        new_user = CustomUser.objects.create_user(
            username="Demo_Student", password="supersecretpassword123"
        )

        # 2. PEEK at the database value
        # If you print the password now, you won't see "supersecretpassword123"
        print(f"Stored Hash: {new_user.password}")

        # 3. VERIFY the password
        # We simulate a login attempt
        login_attempt = "supersecretpassword123"

        # check_password(plain_text, hashed_text)
        if check_password(login_attempt, new_user.password):
            print("Verification Successful: The user is logged in!")

        else:
            print("Verification Failed: Password does not match.")
