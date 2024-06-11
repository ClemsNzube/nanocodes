from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.cache import cache
from .utils import *
from .models import CustomUser
from .serializers import CustomUserSerializer, OTPVerificationSerializer

class UserRegistrationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class VerifyOTPView(generics.CreateAPIView):
    serializer_class = OTPVerificationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            cached_otp = cache.get(email)

            if cached_otp and str(cached_otp) == otp:
                try:
                    user = CustomUser.objects.get(email=email)
                    user.email_verified = True
                    user.save()
                    return Response({"message": "Email verified successfully."}, status=status.HTTP_200_OK)
                except CustomUser.DoesNotExist:
                    return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({"error": "Invalid OTP."}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        try:
            user = CustomUser.objects.get(email=request.data.get('email'))
            if not user.email_verified:
                send_otp(user.email)
                return Response({"error": "Email not verified. OTP sent to email."}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        
        return super().post(request, *args, **kwargs)