from django.urls import path
from .views import UserRegistrationView, VerifyOTPView, CustomTokenObtainPairView

urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='signup'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),


]
