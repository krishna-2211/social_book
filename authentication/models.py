from django.db import models

# Create your models here.
class UserProfile(models.Model):
    username = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.username