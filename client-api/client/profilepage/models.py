from django.db import models

# Create your models here.

# Profile data
class Profile(models.Model):
    nickname = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    premium = models.BooleanField()

    def __str__(self):
        return f'{self.nickname}, {self.status}, {self.premium}'