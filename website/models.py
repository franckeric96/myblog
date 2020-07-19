from django.db import models

# Create your models here.



class SocialAccount(models.Model):
    ICONS = [
        ("facebook", "fa-facebook"),
        ("instagram", "fa-instagram"),
        ("google-plus", "fa-google-plus"),
        ("linkedin", "fa-linkedin-in")
    ]
    
    nom = models.CharField(max_length=255)
    lien = models.URLField()
    icon = models.CharField(choices=ICONS, max_length=20)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Social account'
        verbose_name_plural = 'Socials account'

    def __str__(self):
        return self.nom


class Presentation(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to="images/Presentation")
    slogan = models.TextField(null=True)


    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Presentation'
        verbose_name_plural = 'Presentations'

    def __str__(self):
        return self.nom


class Gallerie(models.Model):
    """Model definition for Gallerie."""
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/Gallerie")

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Gallerie."""

        verbose_name = 'Gallerie'
        verbose_name_plural = 'Galleries'

    def __str__(self):
        """Unicode representation of Gallerie."""
        return self.nom
