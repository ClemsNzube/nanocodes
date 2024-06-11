from django.urls import path
from .views import LogoutView, PasswordResetConfirmView, PasswordResetRequestView, UserRegistrationView, VerifyOTPView, CustomTokenObtainPairView, ChangePasswordView

urlpatterns = [
    path('signup/', UserRegistrationView.as_view(), name='signup'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),
    path('login/', CustomTokenObtainPairView.as_view(), name='login'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password-reset-request/', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password-reset-confirm/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('logout/', LogoutView.as_view(), name='logout'),


]
