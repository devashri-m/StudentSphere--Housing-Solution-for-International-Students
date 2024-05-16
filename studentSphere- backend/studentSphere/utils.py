# utils.py

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import AccessToken

class TokenExpiryCheck(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Access the user from the request
        user = request.user

        # Get the access token from the request headers
        auth_header = request.headers.get('Authorization')
        if auth_header:
            _, token = auth_header.split(' ')
            decoded_token = AccessToken(token)

            # Check if the token is expired
            if decoded_token.is_expired:
                return Response({'message': 'Token has expired'}, status=401)
            else:
                return Response({'message': 'Token is valid'}, status=200)
        else:
            return Response({'message': 'Authorization header not provided'}, status=401)
