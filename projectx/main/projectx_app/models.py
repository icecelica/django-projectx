from django.db import models

# Sign Up.
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    blog_name = models.CharField(max_length=300,unique=True)
    def __str__(self):
        return self.blog_name

class Description(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    description = models.CharField(max_length=400,unique=True)
    def __str__(self):
        return self.description

class AccessRecord(models.Model):
    description = models.ForeignKey(Description, on_delete=models.CASCADE)
    date = models.DateField()
    def __str__(self):
        return str(self.date)

# Signup Model.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) #nnt kat views, kene set 1 to 1..user and profile
    #additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='media/profile_pics',blank=True)

    def __str__(self):
        return self.user.username
