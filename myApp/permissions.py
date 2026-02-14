# myApp/permissions.py
from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # 1. Allow GET, HEAD, or OPTIONS requests for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # 2. Check if the user is even logged in
        if not request.user or not request.user.is_authenticated:
            return False

        # 3. Check if the logged-in user is the owner
        return obj.author == request.user
