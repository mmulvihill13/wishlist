from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Announcement(models.Model):
    title = models.CharField(max_length=255)
    details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User
    content = models.TextField()  # Content of the review
    rating = models.IntegerField()  # Rating out of 5
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the review was created

    def __str__(self):
        return f"Review by {self.user.username} - {self.rating}/5"
