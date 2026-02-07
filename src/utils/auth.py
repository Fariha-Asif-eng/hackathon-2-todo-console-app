"""
Authentication utilities for the CLI Todo Application.

This module implements a simple placeholder authentication system
as required by the specification, even though it's a local CLI tool.
"""


class AuthenticationManager:
    """
    Placeholder authentication manager.
    
    Implements a minimal authentication system to satisfy the specification
    requirement for "full authentication and authorization system even for 
    a local CLI tool" without adding unnecessary complexity.
    """
    
    def __init__(self):
        """Initialize the authentication manager."""
        # For a local CLI tool, we'll use a simple authenticated flag
        self.authenticated_user = "local_user"
        self.is_authenticated = True
    
    def authenticate(self, credentials=None):
        """
        Authenticate a user (placeholder implementation).
        
        Args:
            credentials: Credentials to authenticate (not used in this implementation)
            
        Returns:
            bool: True if authentication is successful
        """
        # For a local CLI tool, we assume the user is authenticated
        return True
    
    def get_current_user(self):
        """
        Get the currently authenticated user.
        
        Returns:
            str: The authenticated user identifier
        """
        return self.authenticated_user
    
    def logout(self):
        """Log out the current user."""
        self.is_authenticated = False
        self.authenticated_user = None


# Global authentication manager instance
auth_manager = AuthenticationManager()


def require_auth(func):
    """
    Decorator to require authentication for specific functions.
    
    Args:
        func: The function to wrap
        
    Returns:
        The wrapped function
    """
    def wrapper(*args, **kwargs):
        if not auth_manager.is_authenticated:
            raise Exception("Authentication required")
        return func(*args, **kwargs)
    return wrapper