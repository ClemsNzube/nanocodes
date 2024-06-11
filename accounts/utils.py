from django.core.mail import send_mail
from django.core.cache import cache
from django.conf import settings
import random

def generate_otp():
    return random.randint(1000, 9999)

def send_otp(email):
    otp = generate_otp()
    cache.set(email, otp, timeout=300)  # Save OTP in cache for 5 minutes
    send_mail(
        'Your OTP Code',
        f'Your OTP code is {otp}',
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
