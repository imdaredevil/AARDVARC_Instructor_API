from rest_framework.authentication import TokenAuthentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token
from django.utils import timezone

class ExpiringTokenAuthentication(TokenAuthentication):
    """
    If token is expired then it will be removed
    and new one with different key will be created
    """
    keyword='Bearer'
    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(key=key)
        except Token.DoesNotExist:
            raise exceptions.AuthenticationFailed("Invalid Token")

        if not token.user.is_active:
            raise exceptions.AuthenticationFailed("User is not active")
        expiryTime = (timezone.now() - token.created).seconds - 3600
        if expiryTime > 0:
            raise exceptions.AuthenticationFailed("The Token is expired")

        return (token.user, token)