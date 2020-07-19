from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    """Model definition for Profile."""
    user = models.OneToOneField(User, verbose_name="profile", on_delete=models.CASCADE)



    nom = models.CharField(max_length=50, null=True)
    contact = models.PositiveIntegerField(null=True)
    date_birthday = models.DateField(auto_now=False, auto_now_add=False, null=True)
    # TODO: Define fields here

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return self.user.username
    
   
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, created, **kwargs):

    instance.profile.save()
    

    
