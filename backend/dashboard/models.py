from django.db import models
from django.contrib.auth.models import User


class UserData(models.Model):
    user = models.ForeignKey(User, on_delete= models.DO_NOTHING)

class Message(models.Model):
    class Meta:
        verbose_name='a message'
        verbose_name_plural='All messages'
    sender = models.ForeignKey(User, on_delete= models.DO_NOTHING, related_name="sender", verbose_name='Your name')
    receiver = models.ForeignKey(User, on_delete= models.DO_NOTHING, related_name="receiver", verbose_name='Select your contact')
    message = models.TextField('Your message')

class Profile(models.Model):
    class Meta:
        verbose_name= 'Profile'
        verbose_name_plural= 'Profiles'
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return self.user.username