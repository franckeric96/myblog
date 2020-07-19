from django.db import models

# Create your models here



class Contact(models.Model):
    message = models.TextField()
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField(max_length=200, null=True)

    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        return self.nom
