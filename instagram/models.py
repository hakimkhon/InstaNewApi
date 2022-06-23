from django.db import models

class Profile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=200, unique=True)
    profil_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.username
    
class Story(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    media = models.FileField(null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.profile)
