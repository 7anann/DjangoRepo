from django.test import TestCase

# Create your tests here.
from .models import Post

"""
class PostModelTest(TestCase):
    def test_post_has_title(self):
        # 1. Setup: Create a dummy object
        post = Post.objects.create(title="Hello World", body="Testing is fun!")

        # 2. Execution: Get the value
        # 3. Assertion: Check if it matches reality
        self.assertEqual(post.title, "Hello World")
"""
'''
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


# 1. THE FIX: Delete the student if they already exist
# This clears the way so 'create_user' doesn't hit a duplicate error
User = get_user_model()
User.objects.filter(username="Demo_Student").delete()


class PostApiTests(APITestCase):

    def setUp(self):
        # This runs BEFORE every individual test
        # We create a user so we can test authentication
        self.user = User.objects.create_user(
            username="testuser", password="password123"
        )
        self.url = reverse("post-list")  # Assuming your URL name is 'post-list'

    def test_get_posts_unauthenticated(self):
        """Test that we get 401 if we aren't logged in"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_posts_authenticated(self):
        """Test that a logged-in user can see posts"""
        # Simulate JWT Authentication
        self.client.force_authenticate(user=self.user)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
'''
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthenticationTests(APITestCase):

    def setUp(self):
        # Create a user to test the login
        self.username = "test_student"
        self.password = "secure_password_123"
        self.user = User.objects.create_user(
            username=self.username, password=self.password
        )
        # Match this name to your urls.py (usually 'token_obtain_pair')
        self.login_url = reverse("token_obtain_pair")

    def test_login_returns_jwt_tokens(self):
        """Test that valid credentials return access and refresh tokens"""
        data = {"username": self.username, "password": self.password}

        response = self.client.post(self.login_url, data, format="json")

        # 1. Check if the status is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 2. Check if 'access' and 'refresh' keys exist in the JSON response
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

        print("\n✅ JWT Token Test Passed: Received access and refresh tokens!")

    def test_token_refresh_logic(self):
        """Test that we can get a new access token using a refresh token"""
        # Step 1: Login to get the initial refresh token
        login_data = {"username": self.username, "password": self.password}
        login_response = self.client.post(self.login_url, login_data, format="json")
        refresh_token = login_response.data["refresh"]

        # Step 2: Hit the refresh endpoint with that token
        # Usually named 'token_refresh' in urls.py
        refresh_url = reverse("token_refresh")
        refresh_data = {"refresh": refresh_token}

        response = self.client.post(refresh_url, refresh_data, format="json")

        # 3. VERIFY: We should get a new 'access' token, but NOT necessarily a new 'refresh'
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)

        print("\n✅ Token Refresh Test Passed: Successfully rotated access token!")


'''
    def test_login_with_wrong_password(self):
        """Test that wrong credentials return 401 Unauthorized"""
        data = {"username": self.username, "password": "wrongpassword"}
        response = self.client.post(self.login_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        print("\n Wrong credentials! 401 Unauthorized")
'''
