from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.contrib.auth import authenticate
from .models import User
from .serializers import RegisterSerializer, LoginSerializer


class RegisterAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            # Prepare the response data with user fields and tokens
            response_data = {
                'status': 'success',
                'message': 'User registered successfully.',
                'user': {
                    'email': user.email,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'role': user.role,
                    'date_joined': user.date_joined,
                    # Include other fields you want to return
                },
                'tokens': {
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }
            }

            # Set the tokens in cookies
            response = Response(response_data, status=status.HTTP_201_CREATED)
            response.set_cookie(
                key='access_token',
                value=str(refresh.access_token),
                httponly=True,
                secure=True,  # Use `True` in production for security
                samesite='Strict',
                max_age=3600  # Set token expiry time in seconds (1 hour here)
            )
            response.set_cookie(
                key='refresh_token',
                value=str(refresh),
                httponly=True,
                secure=True,  # Use `True` in production for security
                samesite='Strict',
                max_age=3600 * 24 * 7  # Set refresh token expiry time (7 days here)
            )
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            user = authenticate(request, email=email, password=password)

            if user:
                refresh = RefreshToken.for_user(user)
                
                # Prepare the response data with user fields and tokens
                response_data = {
                    'status': 'success',
                    'message': 'Login successful.',
                    'user': {
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                        'role': user.role,
                        'date_joined': user.date_joined,
                        # Include other fields you want to return
                    },
                    'tokens': {
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                }

                # Set the tokens in cookies
                response = Response(response_data, status=status.HTTP_200_OK)
                response.set_cookie(
                    key='access_token',
                    value=str(refresh.access_token),
                    httponly=True,
                    secure=True,  # Use `True` in production for security
                    samesite='Strict',
                    max_age=3600  # Set token expiry time in seconds (1 hour here)
                )
                response.set_cookie(
                    key='refresh_token',
                    value=str(refresh),
                    httponly=True,
                    secure=True,  # Use `True` in production for security
                    samesite='Strict',
                    max_age=3600 * 24 * 7  # Set refresh token expiry time (7 days here)
                )
                return response

            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TokenRefreshAPIView(TokenRefreshView):
    """
    SimpleJWT already provides a TokenRefreshView; we can reuse it.
    """
    pass
