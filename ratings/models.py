from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import CustomUser

class Rating(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='rating')
    stars = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    review = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.stars} stars by {self.user.username}'
